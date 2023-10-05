#!/usr/bin/python3
""" This is the '2-matrix_divided' module
"""


def matrix_divided(matrix, div):
    """ This the matrix_divided function
        Args:
            - matrix : List of lists.
            - div (int/float) : The number that will divide the elements of
            matrix.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    len_track = 0
    for item in matrix:
        if type(item) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        len_track += len(item)
    for List in matrix:
        for element in List:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if len_track / len(matrix[0]) != len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for item in matrix:
        row = []
        for element in item:
            row.append(round(element / div, 2))
        new_matrix.append(row)
    return new_matrix
