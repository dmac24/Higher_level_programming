#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """
    Square class, Private instance attribute: size
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        self.__position = value

        if not isinstance(self.__value, [int, int] < 0):
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        else:

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
