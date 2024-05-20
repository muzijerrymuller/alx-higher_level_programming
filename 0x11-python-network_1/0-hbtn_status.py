#!/usr/bin/env python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
# Use a with statement to ensure the response is properly closed after use
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')
    print("\t- {}".format(body))
