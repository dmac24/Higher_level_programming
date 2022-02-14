#!/usr/bin/python3
"""This module contains the "Rectangle" for base class"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Rectangle´s area"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle with the character #"""
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""

        st = "[Rectangle] ({:d}) {:d}/{:d}".format(self.id, self.__x, self.__y)
        st += " - {:d}/{:d}".format(self.__width, self.__height)
        return st
