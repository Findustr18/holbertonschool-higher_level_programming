#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        Method that defines instances of a new rectangle
        Args:
            width: x number of elements
            height: y number of elements
        Raises:
        TypeError: data not an int
        ValueError: data below zero
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """ Getter for width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Setter for width """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Getter for height """
            return self.__height

        @height.setter
        def height(self, value):
            """ Setter for height """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
