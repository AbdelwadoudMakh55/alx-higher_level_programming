#!/usr/bin/python3
""" This is the 101-add_attribute module """


def add_attribute(obj, att_name, value):
    """ This is the add_attribute function """
    if hasattr(obj, '__slots__'):
        if type(type(obj).__slots__) is str:
            if att_name == type(obj).__slots__:
                setattr(obj, att_name, value)
                return
            else:
                raise TypeError("can't add new attribute")
        for attr in type(obj).__slots__:
            if attr == att_name:
                setattr(obj, att_name, value)
                return
        raise TypeError("can't add new attribute")
    else:
        result = 0
        for attr in dir(obj):
            if attr[0] != '_':
                result = 1
                break
        if result == 0:
            setattr(obj, att_name, value)
        else:
            raise TypeError("can't add new attribute")
