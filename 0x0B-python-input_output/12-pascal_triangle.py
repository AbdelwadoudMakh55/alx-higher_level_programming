#!/usr/bin/python3
""" This is the 12-pascal_triangle module """


def pascal_triangle(n):
    """ This the pascal_triangle function """
    if n <= 0:
        return []
    pascal = [[1], [1, 1]]
    for i in range(2, n):
        row = []
        row.append(1)
        for j in range(0, i - 1):
            row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
        row.append(1)
        pascal.append(row)
    return pascal
