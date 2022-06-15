#!/usr/bin/python3
"""0x0C-python-almost_a_circle - rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle - rectangle inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ - inicialize private instance attribute"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Return property width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Set property width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set property height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Return property x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set property x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return property y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set property y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
