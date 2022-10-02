#!/usr/bin/python3
import requests
"""Script that fetches https://intranet.hbtn.io/status"""


req = requests.request('GET', 'https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(req.text))
print("\t- content:", req.text)
