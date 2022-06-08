#!/usr/bin/python3
"""0x0A-python-inheritance - 101-add_attribute.py"""


def add_attribute(self, new_atribute, value):
    """add_atribute - adds a new atribute if it's possible"""
    if not hasattr(self, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(self, new_atribute, value)
