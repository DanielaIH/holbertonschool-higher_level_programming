#!/usr/bin/python3
"""0x0B-python-input_output - 2-append_write.py"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
        return(len(text))
