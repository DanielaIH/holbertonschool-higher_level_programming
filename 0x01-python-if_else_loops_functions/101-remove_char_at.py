#!/usr/bin/python3
def remove_char_at(str, n):
    cp = ""
    for x in range(len(str)):
        if x != n:
            cp += str[x]
    return cp
