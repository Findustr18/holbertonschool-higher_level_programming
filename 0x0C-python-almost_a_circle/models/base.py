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
