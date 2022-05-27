#!/usr/bin/python3
"""
Module 3-saymyname
contains method that prints a name and a last name
takes in two strings
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My names is [full name]"
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                               else "last_name"))
