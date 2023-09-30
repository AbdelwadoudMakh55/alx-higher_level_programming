#!/usr/bin/python3
"""
This is the matrix multplication module.
"""


def matrix_mul(m_a, m_b):
    """ This is the matrix multplication function """
    # First condtion
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    # Second condition
    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
    # Third condition
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for item in m_a:
        if len(item) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for item in m_b:
        if len(m_b) == 0:
            raise ValueError("m_b can't be empty")
    # Fourth condition
    len_m_a = 0
    for item in m_a:
        len_m_a += len(item)
        for element in item:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    len_m_b = 0
    for item in m_b:
        len_m_b += len(item)
        for element in item:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    # Fifth condition
    if len_m_a // len(m_a[0]) != len(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if len_m_b // len(m_b[0]) != len(m_b):
        raise TypeError("each row of m_b must be of the same size")
    # Sixth condition
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Multiplication
    new_matrix = []
    row = [0] * len(m_b[0])
    for i in range(len(m_a)):
        row = [0] * len(m_b[0])
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                row[j] += m_a[i][k] * m_b[k][j]
        new_matrix.append(row)
    return new_matrix
