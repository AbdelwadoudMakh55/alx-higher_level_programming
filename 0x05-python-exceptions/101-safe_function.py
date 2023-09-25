#!/usr/bin/python3
import sys as sy


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as E:
        sy.stderr.write("Exception: {}\n".format(E))
        return None
