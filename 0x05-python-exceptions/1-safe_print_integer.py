#!/usr/bin/python3
def safe_print_integer(value):
    try:
        result = True
        print("{:d}".format(value))
    except ValueError:
        result = False
        return result
    return result
