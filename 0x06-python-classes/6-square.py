#!/usr/bin/python3
""" A Square class definition """


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square
    """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        The position of the Square
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
        value (tuple): position of the square in 2D space
        Returns:
        None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a\
                tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculate the square's area """
        return (self.__size) ** 2

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
