#!/usr/bin/python3
"""0x0A. Python - Inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle - is a DerivedClass"""
    def __init__(self, width, height):
        """__init__ - validates and inizializes width and height
        @width: is the width of the Rectangle
        @height: is the height of the Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """__str__ - returns a rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """area - method that returns the area"""
        return (self.__width * self.__height)


class Square(Rectangle):
    """Square - is a DerivedClass"""
    def __init__(self, size):
        """__init__ - validates and inizializes size
        @size: is the size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
