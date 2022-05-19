#!/usr/bin/python3
""" A Square class definition """


class Square:
    """ Initialization of the class """
    def __init__(self, size=0):

        self.size = size

    def area(self):
        """ Calculate the square's area """
        return self.__size ** 2

    def my_print(self):
        """ Print the square """
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()

    @property
    def size(self):
        """ The size of the square(Getter)
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: sets size to value, if int and >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
