#!/usr/bin/python3
"""0x0B-python-input_output - 1-write_file.py"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return(len(text))
