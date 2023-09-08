#!/usr/bin/python3
def no_c(my_string):
    no_cstring = ""
    for c in my_string:
        if c not in {'c', 'C'}:
            no_cstring += c
    return no_cstring
