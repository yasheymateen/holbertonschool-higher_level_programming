#!/usr/bin/python3
""" Rectangle Class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """ width getter """

            return self.__width

        @width.setter
        def width(self, value):
            """ width setter """

            if type(value) is not int:
                raise TypeError('width must be an integer')
            if value <= 0:
                raise ValueError('width must be > 0')
            self.__width = value

        @property
        def height(self):
            """ height getter """

            return self.__height

        @height.setter
        def height(self, value):
            """ height setter """

            if tyep(value) is not int:
                raise TypeError('height must be an integer')
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value

        @property
        def x(self):
            """ x getter """
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError('x must be an integer')
            if value < 0:
                raise ValueError('x must be >= 0')
            self.__x = value

        @property
        def y(self):
            """ y getter"""

            return self.__y

        @y.setter
        def y(self, value):
            """y setter """

            if type(value) is not int:
                raise TypeError('y must be an integer')
            if value < 0:
                raise ValueError('y must be >= 0')
            self.__y = value

        def area(self):
            """ area """

            return self.width * self.height

        def display(self):
            """ shape"""
            for row in range(self.y):
                print()
            for row in range(self.height):
                print('{}{}'.format(' ' * self.x, '#' * self.width))

        def __str__(self):
            """ str out """

            return '[Rectangle] ({}) {}/{} - {} {}'.format(self.id, self.x,
                                                           self.y, self.width,
                                                           self.height)

        def update(self, *args, **kwargs):
            """ update attrs """
            attrs = ['id', 'width', 'height', 'x', 'y']
            if args and 0 < len(args) <= 5:
                for i, arg in enumerate(args):
                    if i == 0:
                        super().__init__(arg)
                    else:
                        self.__setattr__(attrs[i], arg)
            elif kwargs and 0 < len(kwargs) <= 5:
                for k, v in kwargs.items():
                    if k == 'id':
                        super().__init__(v)
                    elif k in attrs:
                        self.__setattr__(k, v)

        def to_dictionary(self):
            """ returns dict repr """
            return {'id': self.id, 'width': self.width, 'height': self.height,
                    'x': self.x, 'y': self.y}
