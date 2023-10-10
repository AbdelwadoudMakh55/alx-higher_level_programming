#!/usr/bin/python3
""" This is the 2-append_write module """


def append_write(filename="", text=""):
    """ This the write_file function """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
