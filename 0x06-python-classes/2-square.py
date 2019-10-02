#!/usr/bin/python3
""" square Class"""
class Square:
    """class variable size"""
    def __init__(self, size=0):
        """initialize size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
