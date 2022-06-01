#!/usr/bin/python3
"""Rectangle - defines a rectangle"""


class Rectangle():
    """Rectangle - defines a rectangle"""

    def __init__(self, width=0, height=0):
        """The _init_ method defines the properties of Rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """The _str_ method print a Rectangle with #"""
        acum = ""
        if (self.width + self.height > 0):
            for x in range(self.height):
                acum += ("#" * self.width) + "\n"
        return acum[:-1]

    @property
    def width(self):
        """Return property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set property width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set property height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)
