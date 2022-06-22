#!/usr/bin/python3
"""
This modules has a class Mylist that inherits from
list. Has a public instance method print_sorted that
prints the list in ascending order
"""


class MyList(list):
    """inherits from list

    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
