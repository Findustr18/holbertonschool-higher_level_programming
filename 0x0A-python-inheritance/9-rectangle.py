#!/usr/bin/python3
"""
this module contains a class Rectangle
that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation of class.
        width and height must be private. No getter or setter.
        width and height must be positive integers,
        validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
