#!/usr/bin/python3

"""
This module contains the "Rectangle" class
"""

from models.base import Base


class Rectangle:

    """ A Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
