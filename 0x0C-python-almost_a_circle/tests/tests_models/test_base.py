#!/usr/bin/python3
"""
    Conteins tests for Base class.
"""


import unittest
import json
import pep8
import json
import sys
import io
from models import base
from models.base import Base


class TestPep8B(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestBase(unittest.TestCase):
    """
    Class containing functions to test on the Bass class:
        * Functionality.
        * Style.
        * Documentation.
    """
    def SetUp(self):
        """ Method to set the start point """
        Base.Base__nb_objects = 0

    def test_0_id(self):
        """
        Test to chec for id method.
        """
        b0 = Base()
        b1 = Base(23)
        b2 = Base("text")
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 23)
        self.assertEqual(b2.id, "text")

if __name__ == '__main__':
        unittest.main()

# Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
