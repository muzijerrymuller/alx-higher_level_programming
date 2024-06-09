#!/usr/bin/python3
"""
This Python script fetches the URL
'https://alx-intranet.hbtn.io/status' using the 'requests' package.
It displays the body of the response with tabulation before each line.
Only the 'requests' package is allowed for import;
no other packages are permitted.
The output format resembles the following example
(with tabulation before each line):
    - Body response:
    -     <content of the response>
"""
if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
