#!/usr/bin/python3
""" This is the test_rectangle module """


import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ This is the TestBaseClass class """

    def test_construction(self):
        """ Testing the __init__ function """
        s1 = Square(7, 3)
        self.assertAlmostEqual(s1.id, 3)
        self.assertAlmostEqual(s1.size, 7)
        s1.size = 5
        self.assertAlmostEqual(s1.size, 5)
        self.assertAlmostEqual(s1.x, 3)
        self.assertAlmostEqual(s1.y, 0)
        s2 = Square(9, 1, 5, 54)
        self.assertAlmostEqual(s2.id, 54)
        self.assertAlmostEqual(s2.size, 9)
        s2.size = 14
        self.assertAlmostEqual(s2.size, 14)
        self.assertAlmostEqual(s2.x, 1)
        s2.x = 17
        self.assertAlmostEqual(s2.x, 17)
        self.assertAlmostEqual(s2.y, 5)
        s2.y = 20
        self.assertAlmostEqual(s2.y, 20)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)

    def test_val_errors(self):
        """ Test value errors """
        self.assertRaises(ValueError, Square, 0, 5)
        self.assertRaises(ValueError, Square, 0, 0)
        self.assertRaises(ValueError, Square, -5, 10)
        self.assertRaises(ValueError, Square, 10, 5, -3)
        self.assertRaises(ValueError, Square, -5, 0, -3, -4)

    def test_type_errors(self):
        """ Test type errors """
        self.assertRaises(TypeError, Square, "5", 5)
        self.assertRaises(TypeError, Square, 14, 5, True)
        self.assertRaises(TypeError, Square, 10, 5, False)
        self.assertRaises(TypeError, Square, 10, "5")
        self.assertRaises(TypeError, Square, 12, 5, "3")
        self.assertRaises(TypeError, Square, [0], 5)
        self.assertRaises(TypeError, Square, 14, 5, (1,))

    def test_area(self):
        """ This is the test_area function """
        s_area = Square(10)
        self.assertAlmostEqual(s_area.area(), 100)
        s_area.size = 4
        self.assertAlmostEqual(s_area.area(), 16)
        s_area2 = Square(3, 4)
        self.assertAlmostEqual(s_area2.area(), 9)
        s_area2.size = 7
        self.assertAlmostEqual(s_area2.area(), 49)

    def test_update(self):
        """ This is the test_update function """
        s5 = Square(10, 10, 10, 10)
        s5.update(78)
        self.assertAlmostEqual(s5.id, 78)
        s5.update(78, 11, 11, 11)
        self.assertAlmostEqual(s5.id, 78)
        self.assertAlmostEqual(s5.size, 11)
        self.assertAlmostEqual(s5.x, 11)
        self.assertAlmostEqual(s5.y, 11)
        s5.update(size=1, x=2)
        self.assertAlmostEqual(s5.size, 1)
        self.assertAlmostEqual(s5.x, 2)
        s5.update(x=1, y=3, size=4)
        self.assertAlmostEqual(s5.y, 3)
