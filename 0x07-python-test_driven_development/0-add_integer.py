#!/usr/bin/python3
"""
    This is the 0-add_integer module.
"""


def add_integer(a, b=98):
    """ This is the add_integer function.
        Args:
            a (int): The first int.
            b (int): The second int (has default value 98).
        Returns:
            a + b (int): Success.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
