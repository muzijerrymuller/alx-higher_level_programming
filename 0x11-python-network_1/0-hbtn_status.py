#!/usr/bin/env python3
import urllib.request
import ssl

url = 'https://alx-intranet.hbtn.io/status'

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Use a with statement to ensure the response is properly closed after use
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')
    print("\t- {}".format(body))
