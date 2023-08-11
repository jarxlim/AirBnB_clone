#!/usr/bin/python3
"""Unittest module for testing the State class."""

import unittest
from models.state import State
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up the test environment."""
        pass

    def tearDown(self):
        """Tear down the test environment."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test instantiation of the State class."""
        state_obj = State()
        self.assertEqual(str(type(state_obj)), "<class 'models.state.State'>")
        self.assertIsInstance(state_obj, State)
        self.assertTrue(issubclass(type(state_obj), BaseModel))

    def test_attributes(self):
        """Test the attributes of the State class."""
        state_obj = State()
        attributes = ["id", "created_at", "updated_at", "name"]
        for attr in attributes:
            self.assertTrue(hasattr(state_obj, attr))
            
if __name__ == "__main__":
    unittest.main()

