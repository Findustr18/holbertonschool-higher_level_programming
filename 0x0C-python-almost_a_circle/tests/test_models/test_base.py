#!/usr/bin/python3
"""
Module Documentation
Unittest for the base.py file
Tests cases for the class Base
"""
import unittest
import pycodestyle
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class Documentation
    Class created to test the Base Class
    """

    def test_pycodestyle(self):
        """
        Test if the code pass the pycodestyle
        """
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/base.py'])
        self.assertEqual(checker.total_errors, 0)

    def test_documentation(self):
        """
        Test if the code have documentation for each:
        Class and Function
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)

    def test_word_count_documentation(self):
        """
        Test if the Base Class documentation
        Have more than 10 chars.
        """
        num_chars = len(Base.__doc__)
        self.assertGreaterEqual(num_chars, 10)

    def test_word_count_init_documentation(self):
        """
        Test if the Base init function documentation
        Have more than 10 chars.
        """
        num_chars = len(Base.__init__.__doc__)
        self.assertGreaterEqual(num_chars, 10)

    def test_init(self):
        """
        Test that checks the initialization of the 
        Base class with no id
        """
        new_obj = Base()
        self.assertTrue(isinstance(new_obj, Base))
        self.assertGreaterEqual(new_obj.id, 0)

    def test_init_with_id(self):
        """
        Test that checks the initialization of the
        Base Class with an id
        """
        x = 12
        new_obj = Base(x)
        self.assertTrue(isinstance(new_obj, Base))
        self.assertEqual(new_obj.id, x)
