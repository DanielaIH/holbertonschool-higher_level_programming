#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)

    except (IndexError, ZeroDivisionError) as err:
        print("Exception:", err, file=stderr)
        return None
