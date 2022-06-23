#!/usr/bin/python3
"""
this module contains a class called BaseGeometry and
one public instance method "area" that raises an exception
with the message "area() is not implemented"

"""


class BaseGeometry:
    """
    A class base has public instance method
    """
    def area(self):
        """
        Function that raises an exception when called
        """
        raise Exception("area() is not implemented")
