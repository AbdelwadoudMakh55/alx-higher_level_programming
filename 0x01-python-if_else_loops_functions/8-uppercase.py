#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) - 32 if ord(c) <= 122 and ord(c) >= 97
                            else ord(c)), end="")
    print("\n")
