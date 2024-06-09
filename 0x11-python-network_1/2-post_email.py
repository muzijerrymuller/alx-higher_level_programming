#!/usr/bin/python3
"""
This Python script takes a URL and an email as inputs,sends a POST request to the URL with the email as a parameter,
and displays the response body decoded in UTF-8.
Requirements: use only 'urllib' and 'sys' packages, and the 'with' statement.
No need to check input arguments. Test with a server on port 5000
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    parameter = urllib.parse.urlencode(value).encode('ascii')

    request = urllib.request.Request(url, parameter)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
