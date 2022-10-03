#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
from sys import argv

if __name__ == "__main__":
    """Main content"""
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code >= 400:
        print("None")
    else:
        print(response.json()['id'])
