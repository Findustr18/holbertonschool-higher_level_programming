#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains function that creates an object from a "JSON" file
"""


import json


def load_from_json_file(filename):
    """Creates an object from JSON file
    Args:
        filename: file
    """
    with open(filename) as myFile:
        new_obj = json.load(myFile)
    return (new_obj)
