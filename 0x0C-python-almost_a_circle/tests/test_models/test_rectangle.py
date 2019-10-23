#!/usr/bin/python3
""" Unittesting for Class Rectangle """


import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class RectangleTest(unittest.TestCase):
    """ Class Rectangle unittests """

    def test_id_checker(self):
        """ Test if id of Rectangle increments """
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(2, 10)
        self.assertEqual(r3.id, 3)

    def test_input_id(self):
        """ Test if input id gets set """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_check(self):
        """ Test width for rect """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(5, 2, 0, 0, 12)
        self.assertEqual(r3.width, 5)

    def test_check_width_Error_1(self):
        """ Test TypeError for width in rect """
         self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            'string', 2, 0, 0, 12
        )


    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            [6, 4, 9, 9], 2, 0, 0, 12
        )

    def test_check_x(self):
        """Test x of rect"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 6)
        self.assertEqual(r2.x, 6)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 2, 0, 3, 12)
        self.assertEqual(r4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Rect"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, 'string''', 0, 12
        )

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in rect"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, [1, 2, 3, 4], 0, 12
        )

    def test_check_x_ValueError(self):
        """Test ValueError for x in Rect"""
        self.assertRaisesRegex(
            ValueError,
            'x must be >= 0',
            Rectangle,
            4, 2, -1, 0, 12
        )

    def test_check_y(self):
        """Test y of rect"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Rect"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, 'string', 12
        )

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, [1, 2, 3, 4], 12
        )

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rect"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Rectangle,
            4, 2, 0, -6, 12
        )

    def test_update(self):
        """update test"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """update with etra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"


if __name__ == '__main__':
    unittest.main()
