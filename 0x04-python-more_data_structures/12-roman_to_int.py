#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return None
    value = 0
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    4_or9 = {"V": "I", "X": "I", "L": "X", "C": "X", "D": "C", "M": "C"}
    for i in range(1, len(roman_string)):
        if roman_string[i] in val_4or9.keys() 
        and roman_string[i - 1] == val_4or9[roman_string[i]]:
            value += rom[roman_string[i]] - rom[roman_string[i - 1]]
        if roman_string[i] in val_4or9.keys() 
        and roman_string[i - 1] != val_4or9[roman_string[i]]:
            value += rom[roman_string[i]]
        if roman_string[i] == "I" and roman_string[i - 1] == "I":
            value += 1
    if roman_string[len(roman_string) - 1] == 'I':
        value += 1
    if value < rom[roman_string[0]]:
        value += rom[roman_string[0]]
    return value

