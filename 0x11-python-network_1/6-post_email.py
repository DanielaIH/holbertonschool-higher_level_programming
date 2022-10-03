#!/usr/bin/python3
""" script that takes in a URL and an email address,
sends a POST request to the passed URL and finally
displays the body of the response."""


import requests
from sys import argv

if __name__ == "__main__":
    """Main content"""
    req = requests.post(argv[1], {'email': argv[2]})
    print(req.text)
