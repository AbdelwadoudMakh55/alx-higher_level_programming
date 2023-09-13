#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    for num in my_list:
        if num not in uniq:
            uniq.append(num)
    return sum(uniq)
