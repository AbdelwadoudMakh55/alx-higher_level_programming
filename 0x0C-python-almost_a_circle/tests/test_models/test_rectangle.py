#!/usr/bin/python3
""" This is the test_rectangle module """


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ This is the TestBaseClass class """

    def test_construction(self):
        """ Testing the __init__ function """
        r1 = Rectangle(7, 3)
        self.assertAlmostEqual(r1.id, 3)
        self.assertAlmostEqual(r1.width, 7)
        r1.width = 5
        self.assertAlmostEqual(r1.width, 5)
        self.assertAlmostEqual(r1.height, 3)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        r2 = Rectangle(7, 9, 1, 5, 54)
        self.assertAlmostEqual(r2.id, 54)
        self.assertAlmostEqual(r2.width, 7)
        self.assertAlmostEqual(r2.height, 9)
        r2.height = 14
        self.assertAlmostEqual(r2.height, 14)
        self.assertAlmostEqual(r2.x, 1)
        r2.x = 17
        self.assertAlmostEqual(r2.x, 17)
        self.assertAlmostEqual(r2.y, 5)
        r2.y = 20
        self.assertAlmostEqual(r2.y, 20)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)

    def test_val_errors(self):
        """ Test value errors """
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 10, -3)
        self.assertRaises(ValueError, Rectangle, 10, 5, -3)
        self.assertRaises(ValueError, Rectangle, 10, 4, 5, -1)
        self.assertRaises(ValueError, Rectangle, -5, 0, -3, -4)

    def test_type_errors(self):
        """ Test type errors """
        self.assertRaises(TypeError, Rectangle, "5", 5)
        self.assertRaises(TypeError, Rectangle, 14, 5, True)
        self.assertRaises(TypeError, Rectangle, 10, 5, False)
        self.assertRaises(TypeError, Rectangle, 10, "5")
        self.assertRaises(TypeError, Rectangle, 12, 5, "3")
        self.assertRaises(TypeError, Rectangle, 5, 5, 4, "6")
        self.assertRaises(TypeError, Rectangle, [0], 5)
        self.assertRaises(TypeError, Rectangle, 14, 5, (1,))

    def test_area(self):
        """ This is the test_area function """
        r_area = Rectangle(10, 2)
        self.assertAlmostEqual(r_area.area(), 20)
        r_area.height = 4
        self.assertAlmostEqual(r_area.area(), 40)
        r_area2 = Rectangle(3, 3)
        self.assertAlmostEqual(r_area2.area(), 9)
        r_area2.width = 7
        self.assertAlmostEqual(r_area2.area(), 21)

    def test_update(self):
        """ This is the test_update function """
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(78)
        self.assertAlmostEqual(r5.id, 78)
        r5.update(78, 11, 11, 11, 11)
        self.assertAlmostEqual(r5.width, 11)
        self.assertAlmostEqual(r5.height, 11)
        self.assertAlmostEqual(r5.x, 11)
        self.assertAlmostEqual(r5.y, 11)
        r5.update(width=1, x=2)
        self.assertAlmostEqual(r5.width, 1)
        self.assertAlmostEqual(r5.x, 2)
        r5.update(x=1, height=2, y=3, width=4)
        self.assertAlmostEqual(r5.height, 2)
        self.assertAlmostEqual(r5.y, 3)

    def test_to_dict(self):
        """ This is the test_to_dict function """
        r6 = Rectangle(10, 2, 1, 9)
        r6_dictionary = r6.to_dictionary()
        self.assertEqual(r6_dictionary, {'_Rectangle__height': 2, '_Rectangle__width': 10, '_Rectangle__x': 1, '_Rectangle__y': 9, 'id': 4})
        self.assertIsInstance(r6_dictionary, dict)
