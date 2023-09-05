#!/usr/bin/python3
def pow(a, b):
    result = 1
    c = b
    if b < 0:
        b = -b
    for i in range(b):
        result *= a
    if c < 0:
        return 1 / result
    return result
