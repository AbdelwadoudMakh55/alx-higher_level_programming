#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) is False or not a_dictionary:
        return None
    maxi = list(a_dictionary.values())[0]
    best = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > maxi:
            maxi = a_dictionary[key]
            best = key
    return best
