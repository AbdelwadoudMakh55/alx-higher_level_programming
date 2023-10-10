#!/usr/bin/python3
""" This is the 1-write_file module """


def write_file(filename="", text=""):
    """ This the write_file function """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
