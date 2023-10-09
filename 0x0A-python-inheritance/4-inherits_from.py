#!/usr/bin/python3
""" This is the 4-inherits_from module """


def inherits_from(obj, a_class):
    """ This is the inherits_from function """
    if obj.__class__ is a_class:
        return False
    return issubclass(obj.__class__, a_class)
