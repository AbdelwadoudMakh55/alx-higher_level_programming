#!/usr/bin/python3
class MagicClass:
    def __init__(self, MagicClass__radius):
        self._MagicClass__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
