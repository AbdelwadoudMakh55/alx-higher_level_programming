#!/usr/bin/python3
""" This is the 100-nqueen module
"""
import sys


def check_int(string):
    result = 1
    if string[0] == '0':
        return 0
    for i in range(len(string)):
        if string[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = 0
            break
    return result

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
    
