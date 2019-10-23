#!/usr/bin/python3
""" Unittest for Square Size """

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquareSize(unittest.TestCase):
    """ Test Square Size Method """
    def test_size(self):
        self.assertEqual(size(0), 0)
        self.assertEqual(size(4), 4)
        self.assertEqual(size(2.5), 2.5)
        self.assertEqual(size(1), 1)

    def test_value(self):
        self.assertRaises(ValueError, size, -1)

    def test_type(self):
        self.assertRaisesRegex(TypeError, size, True)
        self.assertRaises(TypeError, size, False)
        self.assertRaises(TypeError, size, str)
        self.assertRaises(TypeError, size, [])
        self.assertRaises(TypeError, size, {})

    def test_to_dictionary(self):
        """ Test conv. to dictionary """
        r = Square(1, 1, 1, 1)
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)

if __name__ == '__main__':
    unittest.main()
