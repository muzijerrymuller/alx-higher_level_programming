#!/usr/bin/python3
"""
This script sends a GET request to a specified URL and displays the response body.
If the HTTP status code is 400 or higher, it prints an error message with the status code.
The script uses 'requests' and 'sys' libraries.
URL is provided as a command-line argument.
No error checking for the arguments is performed.
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
