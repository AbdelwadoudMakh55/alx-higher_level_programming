#!/usr/bin/python3
""" This is the 100-my_int module """


class MyInt(int):
    """ This is the MyInt module """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
