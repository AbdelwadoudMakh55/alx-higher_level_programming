#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del_keys = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            to_del_keys.append(key)
    for key in to_del_keys:
        a_dictionary.pop(key)
    return a_dictionary
