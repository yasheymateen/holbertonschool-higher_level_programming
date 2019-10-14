#!/usr/bin/python3
"""
Simple Rectangle
"""


class Rectangle:
    """ Rectangle Class - empty """

    def __init__(self, width=0, height=0):
        """ initializes the width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to find the area of a rectangle """
        return (self.__height) * (self.__width)

    def perimeter(self):
        """ method to find the perimeter of a rectangle """
        if self.__width and self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ string representation of square """
        string = []
        for i in range(self.__height):
            for i in range(self.__width):
                string.append('#')
            string.append('\n')
        x = ''.join(string)
        return x[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(str(self.width), str(self.height))
