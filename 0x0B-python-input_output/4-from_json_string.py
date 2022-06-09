#!/usr/bin/python3
"""0x0B-python-input_output - 4-from_json_string.py"""
import json


def from_json_string(my_str):
    """from_json_string - returns an object represented by a JSON string"""
    return(json.loads(my_str))
