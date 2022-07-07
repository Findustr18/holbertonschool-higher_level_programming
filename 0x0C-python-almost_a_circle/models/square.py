#!/usr/bin/python3
"""
Module contains Class Square that inherits from Rectangle
Inits superclass' id
Contains private size, x, y
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height.
        The width and height must be assigned to the value of size.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def __str__(self):
        """
        Overloading __str__ method should return [Square]
        (<id>) <x>/<y> - <size>
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y,
            self.width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            atribute = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 4:
                    setattr(self, atribute[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
