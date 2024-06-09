#!/usr/bin/python3
"""
This script sends a request to a given URL and
displays the response body (decoded in UTF-8).
Handles urllib.error.HTTPError exceptions,
printing 'Error code: ' followed by the status code.
Uses only 'urllib' and 'sys' packages and the 'with' statement.
No need to check script arguments.
Test with a web server running on port 5000.
"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
    except BaseException:
        pass
