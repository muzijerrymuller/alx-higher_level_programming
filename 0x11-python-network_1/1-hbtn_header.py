#!/usr/bin/python3

"""
Python script to send a request to a given URL and display the
X-Request-Id header value using urllib and sys packages.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
