#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argc = len(sys.argv) - 1
    result = 0
    for x in range(1, argc + 1):
        result += int(sys.argv[x])
    print(f"{result}")
