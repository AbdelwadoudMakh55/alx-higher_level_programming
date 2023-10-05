#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is the Testing class
    """

    def test_return(self):
        """Test the return of the function."""
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([-2, -4, -3]), -2)
