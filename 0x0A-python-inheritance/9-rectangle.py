#!/usr/bin/python3
""" This is the 9-rectangle module """


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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        rect = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return f"{rect}"
