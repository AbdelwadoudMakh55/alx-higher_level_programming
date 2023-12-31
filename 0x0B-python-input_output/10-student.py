#!/usr/bin/python3
""" This is the 10-student module """


class Student:
    """ This is the Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json_rep = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return vars(self)
            for attr in attrs:
                if attr in vars(self).keys():
                    json_rep[attr] = vars(self)[attr]
            return json_rep
        return vars(self)
