#!/usr/bin/python3
"""test module for state class"""
import unittest

from models.base_model import BaseModel
from models.state import State

class TestStat(unittest.TestCase):
    """test case for state class"""

    def setUP(self):
        self.state = State()

    def test_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))