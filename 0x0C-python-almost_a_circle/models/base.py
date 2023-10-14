#!/usr/bin/python3
""" This is the base module """


import json


class Base:
    """ This is the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ This is the to_json_string function """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
