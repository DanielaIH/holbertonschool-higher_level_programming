#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if argc == 0:
        print(f"0 arguments.")
    elif argc == 1:
        print(f"1 argument:")
        print(f"{argc}: {sys.argv[1]}")
    else:
        print(f"{argc} arguments:")
        for x in range(1, argc + 1):
            print(f"{x}: {sys.argv[x]}")
