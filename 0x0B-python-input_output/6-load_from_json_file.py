#!/usr/bin/python3
"""0x0B-python-input_output - 6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """load_from_json_file - function that creates an Object"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
