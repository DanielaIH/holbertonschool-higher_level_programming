#!/usr/bin/python3
from urllib import request
from sys import argv
"""script that takes in a URL, sends a request to
the URL and displays the value of X-Request-Id"""


if __name__ == "__main__":
    """main content"""
    with request.urlopen(argv[1]) as response:
        html = response.headers
    print(html.get('X-Request-Id'))
