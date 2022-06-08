#!/usr/bin/python3
"""0x0A-python-inheritance - 12. My integer"""


class MyInt(int):
    """MyInt - class that inherits from int"""

    def __init__(self, value):
        """__init__ method"""
        self.__value = value

    def __eq__(self, obj):
        """__eq__ method"""
        return self.__value != obj

    def __ne__(self, obj):
        """__ne__ method"""
        return self.__value == obj

