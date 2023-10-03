#!/usr/bin/python3
def magic_string(count=[0]):
    count[0], result = count[0] + 1, ("BestSchool" + ", BestSchool" * count[0])
    return f"{result}"
