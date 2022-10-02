#!/usr/bin/python3
from urllib import request
"""Script that fetches https://intranet.hbtn.io/status"""


with request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode())
