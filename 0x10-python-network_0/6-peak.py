#!/usr/bin/python3
""" This is the find a peak technical interview preparation """


def find_peak(list_of_integers):
    """ This is the function for finding the peak """

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    maxi = max(list_of_integers)
    for n in list_of_integers:
        if n >= maxi:
            return n
