#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
from sys import argv

if __name__ == "__main__":
    """Main content"""
    if len(argv) == 1:
        value = {'q': ""}
    else:
        value = {'q': argv[1]}

    response = requests.post('http://0.0.0.0:5000/search_user', data=value)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
