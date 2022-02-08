#!/usr/bin/python3
from models.base import Base

"""
This module contains the "Rectangle" class
"""


class Rectangle:

    """ A Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.__id = super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """
        Method Name: area
        Purpose: returns area
        """
        return self.__width * self.__height

    def display(self):
        """
        Method Name: display
        Purpose: to display rectangles
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Method Name: __str__
        Purpose: prints params
        """
        s = self
        i = s.id
        x = s.__x
        y = s.__y
        w = s.__width
        h = s.__height
        srt = '[{}] ({}) {}/{} - {}/{}'.format(type(s).__name__, i, x, y, w, h)
        return srt

    def update(self, *args, **kwargs):
        """
        Method Name: update
        Purpose: using *args and **kwargs update attributes
        """
        i = 0
        if len(args) == 0 and not args:
            for k, v in kwargs.items():
                if k is "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v
        else:
            for a in args:
                if i == 0:
                    self.id = a
                if i == 1:
                    self.__width = a
                if i == 2:
                    self.__height = a
                if i == 3:
                    self.__x = a
                if i == 4:
                    self.__y = a
                i += 1

    def to_dictionary(self):
        s = self
        h = "height"
        w = "width"
        i = 'id'
        return {'x': s.__x, 'y': s.__y, i: s.id, h: s.__height, w: s.__width}
