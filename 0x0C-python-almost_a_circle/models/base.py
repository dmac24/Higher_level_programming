#!/usr/bin/python3

"""
This module contains the "Base" class
"""

import json


class Base:

    """ A base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id