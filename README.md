crossRefQuery
=============

A python script to perform CrossRef API queries

This script costructs a CrossRef query for unstructured citation data.
It takes its input from stdin.

forward_match is enabled, so this will allow you to receive email alerts for future queries that are subsequently assigned DOIs.

The format of your stdin input should be:
Username
Password
Email
UniqueQueryID
QueryLine1...
QueryLine2...

