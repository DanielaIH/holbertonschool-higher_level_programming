#!/usr/bin/python3
"""0x0B-python-input_output - 3-to_json_string.py"""
import json

def to_json_string(my_obj):
    """to_json_string - JSON representation of an object"""
    return(json.JSONEncoder().encode(my_obj))
