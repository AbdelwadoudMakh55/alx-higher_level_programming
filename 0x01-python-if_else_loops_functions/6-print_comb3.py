#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i * 10 + i + 1, i * 10 + 10):
        if j != 89:
            print("{:02}, ".format(j), end="")
        else:
            print("{:02}".format(j))
