#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """
    Square class, Private instance attribute: size
    Public instance method: def area(self):
    that returns the current square area
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        for i in range(self.__size):
            if self.__size == 0:
                print()

            print("#" * self.__size)
