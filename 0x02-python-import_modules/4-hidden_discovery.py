#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    f_name = dir(hidden_4)
    f_name.sort()
    for x in f_name:
        if "__" not in x:
            print(f"{x}")
