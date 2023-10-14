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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is the to_json_string function """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This is the save_to_file function """
        if list_objs is not None and len(list_objs) != 0:
            file_name = list_objs[0].__class__.__name__ + ".json"
        else:
            file_name = "Base.json"
        l_dict = []
        with open(file_name, "w", encoding='utf-8') as f:
            for objs in list_objs:
                l_dict.append(vars(objs))
            f.write(cls.to_json_string(l_dict))

    @staticmethod
    def from_json_string(json_string):
        """ This is the from_json_string function """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
