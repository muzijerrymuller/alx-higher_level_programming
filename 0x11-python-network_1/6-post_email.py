#!/usr/bin/python3
"""
This script sends a POST request to a given URL
with an email address as a parameter.
It uses the 'requests' and 'sys' libraries.
The script takes in a URL and an email address as command-line arguments.
The email is sent in the 'email' variable within the POST request.
The response body from the server is then printed out.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
