#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ tests for function max_integer"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3.9, 9.5, 4]), 9.5)
        self.assertEqual(max_integer([-1, -4, -7, -9]), -1)

        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

        with self.assertRaises(TypeError):
            max_integer([1, [2], 3])

if __name__ == '__main__':
    unittest.main()
