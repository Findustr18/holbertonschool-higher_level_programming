#!/usr/bin/python3
"""
this module contains a class called BaseGeometry with
public instance and raises an exception
when required

"""


class BaseGeometry:
    """
    A class base has 2 public instances methods
    """
    def area(self):
        """
        Function that raises an exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value is an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
