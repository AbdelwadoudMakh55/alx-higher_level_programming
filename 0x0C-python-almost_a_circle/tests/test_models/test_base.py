#!/usr/bin/python3
""" This is the test_base module """


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ This is the TestBaseClass class """

    def test_construction(self):
        """ Testing the __init__ function """
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)
        b5 = Base()
        self.assertAlmostEqual(b5.id, 3)
