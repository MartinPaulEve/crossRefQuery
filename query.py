#!/usr/bin/env python

'''
This script costructs a CrossRef query for unstructured citation data.
It takes its input from stdin.

forward_match is enabled, so this will allow you to receive email alerts for future queries that are subsequently assigned DOIs.

The format of your stdin input should be:
Username
Password
Email
UniqueQueryID
QueryLine...
'''

# Copyright (c) 2013 Martin Paul Eve
# Distributed under the GNU GPL v2. For full terms see the file docs/COPYING.

import fileinput
from httplib2 import Http
from urllib import urlencode
from xml.sax.saxutils import escape

queries = []
counter = 0
userinfo = []

# read from stdin
for line in fileinput.input():
	if counter < 4:
		userinfo.append(line.replace("\n", ""))
		counter = counter + 1
	else:
		queries.append(line.replace("\n", ""))

# build the querystring
counter = 1
querystring = ""

querystring = '<?xml version = "1.0" encoding="UTF-8"?><query_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.0" xmlns="http://www.crossref.org/qschema/2.0" xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd"><head><email_address>' + userinfo[2] + '</email_address><doi_batch_id>' + userinfo[3] + '</doi_batch_id></head><body>'

for query in queries:
	if query != "\n":
		querystring = querystring + '<query key="q' + str(counter) + '" enable-multiple-hits="false" forward-match="true"><unstructured_citation>' + escape(query) + '</unstructured_citation></query>'
		counter = counter + 1

querystring = querystring + "</body></query_batch>"

query_params = {"usr": userinfo[0],
		"pwd": userinfo[1],
		"format": "unixref",
		"qdata": querystring}

h = Http()

resp, content = h.request("http://doi.crossref.org/servlet/query?" + urlencode(query_params))
print content

