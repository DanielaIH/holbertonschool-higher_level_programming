#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    f_name = dir(hidden_4)
    #f_name.sort()
    for x in f_name:
        if "__" not in x:
            print(x)
