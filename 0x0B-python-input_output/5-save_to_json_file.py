#!/usr/bin/python3
""" This is the 5-save_to_json_file module """


import json


def save_to_json_file(my_obj, filename):
    """ This the save_to_json_file function """
    with open(filename, "w", encoding='utf-8') as f:
        if type(my_obj) != str:
            return f.write(json.dumps(my_obj))
        else:
            return f.write(my_obj)
