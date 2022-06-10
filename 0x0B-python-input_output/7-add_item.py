#!/usr/bin/python3
"""0x0B-python-input_output - 7-add_item.py"""
from sys import argv
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """main function"""
    my_list = []
    if exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    args = argv[1:]
    for x in args:
        my_list.append(x)
    save_to_json_file(my_list, "add_item.json")

