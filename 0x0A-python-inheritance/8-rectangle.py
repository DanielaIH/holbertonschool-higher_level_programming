#!/usr/bin/python3
"""0x0A. Python - Inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle - is a DerivedClass"""
    def __init__(self, width, height):
        """__init__ - validate and inizialize width and height
        @width: is the width of the Rectangle
        @height: is the height of the Rectangle
        """
        if (super().integer_validator("width", width)):
            self.__width = width
        if (super().integer_validator("height", height)):
            self.__height = height
