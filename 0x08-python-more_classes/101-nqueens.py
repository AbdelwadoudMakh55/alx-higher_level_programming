#!/usr/bin/python3
""" This is the 100-nqueen module
"""
import sys


def check_int(string):
    result = 1
    if string[0] == '0' and len(string) != 1:
        return 0
    for i in range(len(string)):
        if string[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = 0
            break
    return result

def bounding_function(mat):
    for i in range(len(mat)):
        sum_row = 0
        for j in range(len(mat)):
            sum_row += mat[i][j]
        if sum_row > 1:
            return 0

    for i in range(len(mat)):
        sum_col = 0
        for j in range(len(mat)):
            sum_col += mat[j][i]
        if sum_col > 1:
            return 0

    sum_diag1 = 0
    for i in range(len(mat)):
        sum_diag1 += mat[i][i]
    if sum_diag1 > 1:
        return 0

    sum_diag2 = 0
    for i in range(len(mat)):
        sum_diag2 += mat[len(mat) - 1 - i][i]
    if sum_diag2 > 1:
        return 0
    return 1

def nqueen(n):
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not check_int(sys.argv[1]):
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4");
        sys.exit(1)

    row = int(sys.argv[1])
    chess_board = []
    for i in range(row):
        line = []
        for j in range(row):
            line.append(0)
        chess_board.append(line)

    count_placement = 0
