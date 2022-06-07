#!/usr/bin/python3
"""print_sorted - class MyList that inherits from list"""


def print_sorted(self):
    """prints the list, ascending sorted"""
    list2 = self + []
    list2.sort()
    print(list2)
