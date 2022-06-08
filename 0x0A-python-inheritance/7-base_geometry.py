#!/usr/bin/python3
"""Area - is an empty module"""


class BaseGeometry():
    """Area is not implemented"""
    def area(self):
        """Area is not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer_validator - validate value"""
        self.name = name
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        else:
            self.value = value
