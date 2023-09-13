#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        new_matrix = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[i][j] ** 2)
            new_matrix.append(row)
        return new_matrix
