#!/usr/bin/python3
import hidden_4 as hd
f_name = dir(hd)
f_name.sort()
for x in f_name:
    if "__" not in x:
        print(x)
