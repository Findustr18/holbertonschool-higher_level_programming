#!/usr/bin/python3
"""
Module 11-student
Write a class Student to disk and reload
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

    def reload_from_json(self, json):
        """
        Method  that replaces all attributes of the Student instance
        json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
