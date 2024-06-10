#!/usr/bin/python3
"""
This script gathers your GitHub credentials (username and password),
then proceeds to interact with the GitHub API
to fetch and display your user ID.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
