#!/usr/bin/python3
""" This is the 6-load_from_json_file module """


import json


def load_from_json_file(filename):
    """ This the load_from_json_file function """
    with open(filename, "r", encoding='utf-8') as f:
        return json.loads(f.read())
