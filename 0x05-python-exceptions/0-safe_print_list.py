#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            result = i + 1
        print("")
    except IndexError:
        return result
    return result
