#!/usr/bin/python3
""" Class Rectangle """


from multiprocessing.sharedctypes import Value


class Rectangle:
    """ class that defines a rectangle
    Args:
        width (int): width
        height (int): height

        Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Method that defines instances of a new rectangle """
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
            if value < 0:
                raise ValueError("width must be >= 0")
            self.width = value

        @property
        def height(self):
            """ Getter for height """
            return self.height

        @height.setter
        def height(self, value):
            """ Setter for height """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.height = value

    def area(self):
        """ Returns width * height """
        return self.height * self.width

    def perimeter(self):
        """ Returns width*2 + height*2(or return 0 if width or height is 0) """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
