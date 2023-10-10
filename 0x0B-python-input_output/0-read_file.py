#!/usr/bin/python3
""" This is the 0-read_file module """


def read_file(filename=""):
    """ This the read_file function """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
