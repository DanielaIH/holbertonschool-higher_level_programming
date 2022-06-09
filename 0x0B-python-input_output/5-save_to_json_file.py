#!/usr/bin/python3
"""0x0B-python-input_output - 5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file -  writes an Object to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
