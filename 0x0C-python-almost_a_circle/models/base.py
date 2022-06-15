#!/usr/bin/python3
"""0x0C-python-almost_a_circle - base.py"""


from models.__init__ import __init__

class Base():
    __nb_objects = 0
    """Class Base - base of all other classes in this project"""
    def __init__(self, id=None):
        """__init__ - inicialize private class attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
