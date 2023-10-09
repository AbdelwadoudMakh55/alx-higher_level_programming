#!/usr/bin/python3
""" This is the 8-rectangle module """


class BaseGeometry:
    """ This is the BaseGeometry class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ This is the rectangle module """

    def __init__(self, width, height):
        """ This the instantiation module """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
