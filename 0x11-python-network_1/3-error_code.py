#!/usr/bin/python3
"""script that takes in a URL, and sends a request to
the URL and displays the body of the response"""

from urllib import request, parse, error
from sys import argv


if __name__ == "__main__":
    """main content"""
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode())

    except error.HTTPError as e:
        print("Error code:", e.code)
