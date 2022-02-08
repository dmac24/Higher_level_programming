#!/usr/bin/python3
from models.rectangle import Rectangle

"""
This module contains the "square" class
"""


class Square(Rectangle):

    """ A Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(Rectangle):
        s = Rectangle
        i = s.id
        x = s.x
        y = s.y
        w = s.width
        srt = '[{}] ({}) {}/{} - {}'.format(type(s). __name__, i, x, y, w)
        return srt

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, vari):
        if not isinstance(self.width, int):
            raise TypeError("size must be an integer")
        if self.width <= 0:
            raise ValueError("size must be > 0")
        self.width = vari
        self.height = vari

    def update(self, *args, **kwargs):
        i = 0
        s = Rectangle
        if len(args) == 0 and not args:
            for k, v in kwargs.items():
                if k is "id":
                    s.id = v
                if k == "size":
                    s.width = v
                if k == "x":
                    s.x = v
                if k == "y":
                    s.y = v
        else:
            for a in args:
                if i == 0:
                    s.id = a
                if i == 1:
                    s.width = a
                if i == 2:
                    s.x = a
                if i == 3:
                    s.y = a
                i += 1

    def to_dictionary(self):
        s = self
        return {'id': s.id, 'x': s.x, 'size': s.width, 'y': s.y}def __init__(self, size, x=0, y=0, id=None):
        """class Constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(Rectangle):
        s = Rectangle
        i = s.id
        x = s.x
        y = s.y
        w = s.width
        srt = '[{}] ({}) {}/{} - {}'.format(type(s). __name__, i, x, y, w)
        return srt

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, vari):
        """ s """
        if not isinstance(self.width, int):
            raise TypeError("size must be an integer")
        if self.width <= 0:
            raise ValueError("size must be > 0")
        self.width = vari
        self.height = vari

    def update(self, *args, **kwargs):
        i = 0
        s = Rectangle
        if len(args) == 0 and not args:
            for k, v in kwargs.items():
                if k is "id":
                    s.id = v
                if k == "size":
                    s.width = v
                if k == "x":
                    s.x = v
                if k == "y":
                    s.y = v
        else:
            for a in args:
                if i == 0:
                    s.id = a
                if i == 1:
                    s.width = a
                if i == 2:
                    s.x = a
                if i == 3:
                    s.y = a
                i += 1

    def to_dictionary(self):
        s = self
        return {'id': s.id, 'x': s.x, 'size': s.width, 'y': s.y}
