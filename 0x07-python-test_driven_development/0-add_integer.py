#!/usr/bin/python3
"""
Function that adds two integers
a and b must be integers or floats,
otherwaise rise a TypeError exception with the
message a must be an integer or b must be an integer.
a and b must be first casted to integers if they are float.
"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a: first int
        b: second int

    Rises:
        TypeError: If a or b are not int or float.

    Returns:
        The sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
