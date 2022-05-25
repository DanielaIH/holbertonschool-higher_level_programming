#!/usr/bin/python3
"""class Square - a class that defines a square"""


class Square:
    """
    class Square - a class that defines a square

   __init__: creates a square object.

    Atributes:
        __size (no type/value verification)
    """
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

