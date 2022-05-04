#!/usr/bin/python3
for x in range(89):
    if x < int(str(x).zfill(2)[1]+str(x).zfill(2)[0]):
        print(f"{x:02}", end=", ")
print(f"{89:02}")
