#!/usr/bin/python3
"""
Write the first class Base
Contains private class __nb_objects, and class constructor __init__
Returns JSON string representation of list dictionaries
"""


import json


class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
            to_json_string(list_dictionaries)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize id, increment class attribute if no
        id and set as id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string representation of list dict """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON strings of all instances into a file
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))
