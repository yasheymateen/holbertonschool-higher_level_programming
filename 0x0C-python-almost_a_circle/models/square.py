#!/usr/bin/python3
"""Square Class Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size Getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size Setter"""

        self.width = value
        self.height = value

    def __str__(self):
        """str  out"""

        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attrs"""

        attrs = ['id', 'size', 'x', 'y']
        if args and 0 < len(args) <= 4:
            for i, arg in enumerate(args):
                if i == 0:
                    super().update(arg)
                else:
                    self.__setattr__(attrs[i], arg)
        elif kwargs and 0 < len(kwargs) <= 4:
            for k, v in kwargs.items():
                if k == 'id':
                    super().update(id=v)
                elif k in attrs:
                    self.__setattr__(k, v)

    def to_dictionary(self):
        """Return dict repr"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
