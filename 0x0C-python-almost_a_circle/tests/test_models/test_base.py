#!/usr/bin/python3
""" Unit testing for Base class """


import unittest
import sys
from models import Base
from  models.base import Base

from io import StringIO

class BaseTest(unittest.TestCase):
    """ Class Base unittests"""

    def test_incrementation(self):
        """ obj id increments """
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_inputs(self):
        """checks for valid input """
        Base._Base__nb_objects = 0

        b_zero = Base()
        self.assertEqual(b_zero.id, 1)

        b_int = Base(17)
        self.assertEqual(b_int.id, 17)

        b_negint = Base(-29)
        self.assertEqual(b_negint.id, -29)

    def test_creation(self):
        """ test instantiation with create """

        dr1 = {'id': 1, 'width': 3, 'height': 5, 'x': 2, 'y': 4}
        r1 = Rectangle.create(**dr1)
        self.assertEqual(r1.to_dictionary(), dr1)
        self.assertEqual(Base._Base__nb_objects, 1)

        ds1 = {'id': 1, 'size': 3, 'x': 2, 'y': 4}
        s1 = Square.create(**ds1)
        self.assertEqual(s1.to_dictionary(), ds1)
        self.assertEqual(Base._Base__nb_objects, 2)

        r2 = Rectangle(3, 5, 2, 4, 1)
        dr2 = r2.to_dictionary()
        r3 = Rectangle.create(**dr2)
        self.assertEqual(r3.to_dictionary(), dr2)
        self.assertEqual(Base._Base__nb_objects, 3)


        r4 = Rectangle(3, 5, 2, 4)
        dr4 = r4.to_dictionary()
        r5 = Rectangle.create(**dr4)
        self.assertEqual(r5.to_dictionary(), dr4)
        self.assertEqual(Base._Base__nb_objects, 5)

        r6 = Rectangle(3, 5)
        dr6 = r6.to_dictionary()
        r7 = Rectangle.create(**dr6)
        self.assertEqual(r7.to_dictionary(), dr6)
        self.assertEqual(Base._Base__nb_objects, 7)

        s2 = Square(3, 2, 4, 1)
        ds2 = s2.to_dictionary()
        s3 = Square.create(**ds2)
        self.assertEqual(s3.to_dictionary(), ds2)
        self.assertEqual(Base._Base__nb_objects, 8)

        s4 = Square(3, 2, 4)
        ds4 = s4.to_dictionary()
        s5 = Square.create(**ds4)
        self.assertEqual(s5.to_dictionary(), ds4)
        self.assertEqual(Base._Base__nb_objects, 10)

        s6 = Square(3, 2)
        ds6 = s6.to_dictionary()
        s7 = Square.create(**ds6)
        self.assertEqual(s7.to_dictionary(), ds6)
        self.assertEqual(Base._Base__nb_objects, 12)
    def test_load_from_file(self):
        """Test load_from_file method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()

        Rectangle.save_to_file([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file()
        Square.save_to_file([s1, s2, s3])
        list_objs_s = Square.load_from_file()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)
if __name__ == '__main__':
    unittest.main()
