#!/usr/bin/python3
"""
Write the first class Base
"""


class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
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
