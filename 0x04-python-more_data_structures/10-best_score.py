#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        max = a_dictionary.values()[0]
        for key in a_dictionary.keys():
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                best = key
        return best
    return None
