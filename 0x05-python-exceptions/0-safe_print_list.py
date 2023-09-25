#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x + 1):
            print(f"{my_list[i]}", end="")
            result = i + 1
    except IndexError:
        print("")
        return result
    print("")
    return result
