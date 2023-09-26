#!/usr/bin/python3
"""This is the 4-square module
Classes:
    - 'Square': This the class of squares.
"""


class Square:
    """ This the square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) and position[0] <= 0 \
           and not isinstance(position[1], int) and position[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and value[0] <= 0 \
           and not isinstance(value[1], int) and value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
