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
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        listy = []
        extra = len("_Rectangle__")
        filename = cls.__name__ + ".json"
        for objects in list_objs:
            listy.append(objects.__dict__)
        dicty = json.loads(json.dumps(listy))
        for x in dicty:
            for i in x:
		if len(i) > extra:
			i = i[extra:]
                print("dicty --", i, x[i])

        with open(filename, 'w') as f:
            f.write(Base.to_json_string(listy))
