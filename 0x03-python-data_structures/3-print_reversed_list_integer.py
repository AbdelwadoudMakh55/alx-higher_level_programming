#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list[::-1]
    for i in range(len(my_list)):
        print("{:d}".format(new_list[i]))
