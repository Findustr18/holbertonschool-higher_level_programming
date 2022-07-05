#!/usr/bin/python3
"""
Module Documentation
Unittest for the rectangle.py file
Tests cases for the class Rectangle
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class Documentation
    Class created to test the Rectangle Class
    """

    def test_pycodestyle(self):
        """
        Test if the code pass the pycodestyle
        """
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/rectangle.py'])
        self.assertEqual(checker.total_errors, 0)

    def test_documentation(self):
        """
        Test if the code have documentation for each:
        Class and Function
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)

    def test_word_count_documentation(self):
        """
        Test if the Rectangle Class documentation
        Have more than 10 chars.
        """
        num_chars = len(Rectangle.__doc__)
        self.assertGreaterEqual(num_chars, 10)
        num_chars = len(Rectangle.__init__.__doc__)
        self.assertGreaterEqual(num_chars, 10)
        num_chars = len(Rectangle.height.__doc__)
        self.assertGreaterEqual(num_chars, 10)
        num_chars = len(Rectangle.width.__doc__)
        self.assertGreaterEqual(num_chars, 10)
        num_chars = len(Rectangle.x.__doc__)
        self.assertGreaterEqual(num_chars, 1)
        num_chars = len(Rectangle.y.__doc__)
        self.assertGreaterEqual(num_chars, 1)
      
    def test_init(self):
        """
        Test that checks the initialization of the 
        Rectangle class with no id, but with a Width and a Height.
        """
        new_obj = Rectangle(5, 10)
        self.assertTrue(isinstance(new_obj, Rectangle))
        self.assertGreaterEqual(new_obj.id, 0)

    def test_init_2(self):
        """
        Test that checks the initialization of the
        Rectangle Class with no id, but with a Width, a Height
        an X and a Y.
        """
        new_obj = Rectangle(5, 10, 1, 2)
        self.assertTrue(isinstance(new_obj, Rectangle))
        self.assertGreaterEqual(new_obj.id, 0)

    def test_init_3(self):
        """
        Test that checks the initialization of the
        Rectangle Class with id, but with a Width, a Height
        an X and a Y.
        """
        id = 12
        new_obj = Rectangle(5, 10, 1, 2, id)
        self.assertTrue(isinstance(new_obj, Rectangle))
        self.assertEqual(new_obj.id, id)

    def test_inheritance(self):
        """
        Test that checks the inheritance.
        """
        new_obj = Rectangle(5, 10)
        self.assertTrue(isinstance(new_obj, Rectangle))
        self.assertTrue(isinstance(new_obj, Base))
