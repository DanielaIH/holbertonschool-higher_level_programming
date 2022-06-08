#!/usr/bin/python3
"""0x0A. Python - Inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square - is a DerivedClass"""
    def __init__(self, size):
        """__init__ - validates and inizializes size
        @size: is the size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
