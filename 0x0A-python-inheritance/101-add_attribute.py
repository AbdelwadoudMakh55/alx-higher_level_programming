#!/usr/bin/python3
""" This is the 101-add_attribute module """


def add_attribute(obj, att_name, value):
    """ This is the add_attribute function """
    result = 0
    for attr in dir(obj):
        if attr[0] != '_':
            result = 1
            break
    if result == 0:
        setattr(obj, att_name, value)
    else:
        raise TypeError("can't add new attribute")
