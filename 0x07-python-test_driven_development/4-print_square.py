#!/usr/bin/python3
"""
This is the '4-print_square' module.
"""


def print_square(size):
    """This is the print_square function
    Args:
        -size (int) : Length of square.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
