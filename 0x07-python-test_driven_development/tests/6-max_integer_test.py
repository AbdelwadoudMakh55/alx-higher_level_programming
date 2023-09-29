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

    def test_type(self):
        """ Test the type of value """
        self.assertRaises(TypeError, max_integer, "abcd")
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, 5.23)
        self.assertRaises(TypeError, max_integer, (5, 3))
        self.assertRaises(TypeError, max_integer, {2, 10})
        self.assertRaises(TypeError, max_integer, True)

    def test_value(self):
        """ Test the value """
        self.assertRaises(ValueError, max_integer, [[5, 6]])
        self.assertRaises(ValueError, max_integer, ["abcd", 5])
        self.assertRaises(ValueError, max_integer, [5.36, 5])
        self.assertRaises(ValueError, max_integer, [(5, 3)])
        self.assertRaises(ValueError, max_integer, [{1, "abc"}, 11])
