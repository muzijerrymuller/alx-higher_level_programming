#!/usr/bin/python3
"""
This Python script sends a request to a given
URL using the 'requests' package.
It extracts and displays the value of the
'X-Request-Id' variable from the response header.
The 'X-Request-Id' variable holds a unique identifier for each request.
Only the 'requests' and 'sys' packages are allowed
for import; no other packages are permitted.
No need to check script arguments (number and type).
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
