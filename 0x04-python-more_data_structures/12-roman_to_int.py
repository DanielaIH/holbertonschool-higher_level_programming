#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_k = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    number = 0
    for i in range(len(roman_string)):
        if i+1 < len(roman_string) and roman_string[i:i+2] in roman_k:
            number += roman_k[roman_string[i:i+2]]
            i += 2
        else:
            number += roman_k[roman_string[i]]
            i += 1
    return number
