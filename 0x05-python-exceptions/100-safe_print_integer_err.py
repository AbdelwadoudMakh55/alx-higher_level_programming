#!/usr/bin/python3
import sys as sy
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as Verr:
        sy.stderr.write("Exception: {}\n".format(Verr))
        return False
    except TypeError as Terr:
        sy.stderr.write("Exception: {}\n".format(Terr))
        return False
    return True
