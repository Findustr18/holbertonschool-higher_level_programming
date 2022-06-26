#!/usr/bin/python3
"""
Module 8-class_to_json
Contains function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """Returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj: python object
    """
    return obj.__dict__
