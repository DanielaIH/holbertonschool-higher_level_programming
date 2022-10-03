#!/usr/bin/python3
import requests
from sys import argv
"""Script that  takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id"""


req = requests.get(argv[1])
print(req.headers['X-Request-Id'])
