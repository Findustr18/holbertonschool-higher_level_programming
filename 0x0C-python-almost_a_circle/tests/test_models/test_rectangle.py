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
from io import StringIO
from contextlib import redirect_stdout


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

    """ Test methods """
    def test_area(self):
        """ Test method: Area """
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_print(self):
        """Test method: __str__"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test method: update(*args)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        """Test method: update(*kwargs)"""
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        """Test mixture of valid and invalid *kwargs"""
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')
    