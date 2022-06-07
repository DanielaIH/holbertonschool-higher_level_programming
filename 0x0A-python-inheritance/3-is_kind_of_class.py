#!/usr/bin/python3
"""is_kind_of_class - check if an object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class"""


def is_kind_of_class(obj, a_class):
    """check if is an object is instance"""
    return(isinstance(obj, a_class))
