#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if (ord(x) >= 97):
            x = chr(ord(x) - 32)
        print(x, end="")
    print()
