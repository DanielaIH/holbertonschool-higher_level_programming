#!/usr/bin/python3
"""0x0B-python-input_output - 9-student.py"""


class Student():
    """Student - defines a student"""
    def __init__(self, first_name, last_name, age):
        """Inicialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json - retrieves a dictionary representation"""
        return self.__dict__
