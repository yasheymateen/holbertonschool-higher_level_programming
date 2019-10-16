#!/usr/bin/python3
""" basegeometry class """


class BaseGeometry:
    """ calculations """

    def area(self):
        """ area calculations """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" rectangle class that inherits from basegeometry"""

class Rectangle(BaseGeometry):
    """ Rectangle class"""

    def __init__(self, width, height):
        """ instantiation """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ string """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

""" class square that inherits from rectangle """

class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """ instantiation """
        self.__size = size
        super().__init__(self.__size, self.__size)
