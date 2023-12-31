#!/usr/bin/python3
""" This is the 7-add_item module """


import json
import sys
from pathlib import Path


def save_to_json_file(my_obj, filename):
    """ This the save_to_json_file function """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """ This the load_from_json_file function """
    with open(filename, "r", encoding='utf-8') as f:
        return json.loads(f.read())


def main():
    """ This is the main function"""
    path = Path("./add_item.json")
    if path.is_file():
        p_list = load_from_json_file("add_item.json")
        if type(p_list) is not list:
            save_to_json_file([], "add_item.json")
            p_list = load_from_json_file("add_item.json")
    else:
        save_to_json_file([], "add_item.json")
    p_list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        p_list.append(sys.argv[i])
        save_to_json_file(p_list, "add_item.json")


main()
