#!/usr/bin/python3
"""This the module 103-magic_class
- Classes:
    - 'MagicClass' : This is a class that do magic stuff."""


class MagicClass:
    """ This is the MagicClass """
    def __init__(self, radius):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
