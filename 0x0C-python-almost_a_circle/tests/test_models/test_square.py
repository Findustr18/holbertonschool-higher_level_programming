#!/usr/bin/python3
"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""


import unittest
import pycodestyle
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestPycodestyle(unittest.TestCase):
    """Pycodestyle models/square.py & tests/test_models/test_square.py"""
    def test_pycodestyle(self):
        """Pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pycodestyle')


class TestBase(unittest.TestCase):
    """Tests for models/square.py"""

    """Test attributes"""
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        s1 = Square(9, 99, 999, 1000)
        self.assertTrue(s1.width == 9)
        self.assertTrue(s1.height == 9)
        self.assertTrue(s1.size == 9)
        self.assertTrue(s1.x == 99)
        self.assertTrue(s1.y == 999)
        self.assertTrue(s1.id == 1000)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        s2 = Square(88)
        self.assertTrue(s2.width == 88)
        self.assertTrue(s2.height == 88)
        self.assertTrue(s2.size == 88)
        self.assertTrue(s2.x == 0)
        self.assertTrue(s2.y == 0)
        self.assertTrue(s2.id is not None)
