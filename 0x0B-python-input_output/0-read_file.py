#!/usr/bin/python3
"""0x0B-python-input_output - 0-read_file.py"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
