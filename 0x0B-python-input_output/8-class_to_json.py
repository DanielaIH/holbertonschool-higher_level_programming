#!/usr/bin/python3
"""0x0B-python-input_output - 8-class_to_json.py"""


def class_to_json(obj):
    """class_to_json - returns the dictionary description"""
    new_dict = obj.__dict__
    return new_dict
