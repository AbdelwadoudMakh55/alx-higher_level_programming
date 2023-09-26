#!/usr/bin/python3
"""This is the 3-square module
Classes:
    - 'Square': This the class of squares.
"""


class Square:
    """ This the square class.
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
