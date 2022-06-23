#!/usr/bin/python3
"""
this module contains a class Square
that inherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, size):
        """
        Instantiation of class.
        size must be private. No getter or setter.
        size must be positive integers,
        validated by integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the area of the rectangle """
        return self.__size ** 2

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
