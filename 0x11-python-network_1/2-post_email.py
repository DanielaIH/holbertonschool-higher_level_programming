#!/usr/bin/python3
"""script that takes in a URL, and sends a POST request to
the passed URL with the email as a parameter"""

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    """main content"""
    post_data = parse.urlencode({"email": argv[2]}).encode()

    with request.urlopen(request.Request(argv[1], post_data)) as response:
        print(response.read().decode('utf-8'))
