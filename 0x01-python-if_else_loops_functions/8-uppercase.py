#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if i == len(str) - 1:
            print("{:c}".format(ord(str[i]) - 32 if ord(str[i]) <= 122 and
                                ord(str[i]) >= 97 else ord(str[i])))
        else:
            print("{:c}".format(ord(str[i]) - 32 if ord(str[i]) <= 122 and
                                ord(str[i]) >= 97 else ord(str[i])), end="")
