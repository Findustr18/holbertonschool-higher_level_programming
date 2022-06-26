#!/usr/bin/python3
"""
Module 10-student
Write a class Student with filter
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        class Student that defines a student by:
        first_name
        last_name
        age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation
        of a Student
        Return:
        a dictionary representation of a student
        instance with specified attributes
        """
        if attrs is None:
            return self.__dict__

        dictt = {}
        for i in attrs:
            if i in self.__dict__:
                dictt[i] = self.__dict__[i]
        return dictt
