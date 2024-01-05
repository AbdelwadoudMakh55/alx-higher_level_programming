#!/usr/bin/python3
""" This is the find a peak technical interview preparation """

def find_peak(list_of_integers):
    """ This is the function for finding the peak """

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    list_copy = list_of_integers[:]
    list_copy1 = list_of_integers[:]
    list_copy.sort()
    list_copy1.sort(reverse=True)
    if list_of_integers == list_copy:
        return list_of_integers[len(list_of_integers) - 1]
    if list_of_integers == list_copy1:
        return list_of_integers[0]
    maxi = max(list_of_integers)
    return maxi
