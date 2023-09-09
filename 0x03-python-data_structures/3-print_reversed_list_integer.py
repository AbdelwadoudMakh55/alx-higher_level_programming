#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("", end="")
    else:
        new_list = my_list[::-1]
        for integer in new_list:
            print("{:d}".format(integer))
