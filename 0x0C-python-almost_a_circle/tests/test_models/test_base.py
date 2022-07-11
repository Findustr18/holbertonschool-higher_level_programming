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

    """Test attributes"""
    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """Test ids match incremented nb_objects when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    """Test args given"""
    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    """Test class"""
    def test_class(self):
        """Test class created is indeed Base"""
        self.assertTrue(Base(100), self.__class__ == Base)

    """Test Python obj to JSON"""
    def test_to_json_string(self):
        """Test dict given translates into JSON string"""
        d0 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        strd01 = Base.to_json_string([d0, d1])
        self.assertTrue(type(d0) == dict)
        self.assertTrue(type(strd01) == str)
        self.assertTrue(strd01,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_none_to_json_string(self):
        """Test no dict given translates into JSON string of empty dict"""
        d2 = None
        strd2 = Base.to_json_string([d2])
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty dict"""
        d3 = dict()
        strd3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3, "[]")

    """Test JSON to Python obect"""
    def test_from_json_string(self):
        """Test JSON string translates into Python dict"""
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs0[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_none_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_from_empty_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])
