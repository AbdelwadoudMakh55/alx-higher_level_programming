#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print(f"{my_list[i]:d}", end="")
            result += 1
        except (ValueError, TypeError):
            pass
    print("")
    return result
