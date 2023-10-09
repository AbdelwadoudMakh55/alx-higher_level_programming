#!/usr/bin/python3
""" This is the 1-my_list module
"""


class MyList(list):
    """ This the MyList class """

    def print_sorted(self):
        """ This the print sorted function """
        a = self[:]
        a.sort()
        print(a)
