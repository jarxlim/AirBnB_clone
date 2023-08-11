#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

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
        """Test instantiation of the Amenity class."""
        amenity_obj = Amenity()
        self.assertEqual(str(type(amenity_obj)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_obj, Amenity)
        self.assertTrue(issubclass(type(amenity_obj), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Amenity class."""
        amenity_obj = Amenity()
        attributes = ["id", "created_at", "updated_at", "name"]
        for attr in attributes:
            self.assertTrue(hasattr(amenity_obj, attr))
            
if __name__ == "__main__":
    unittest.main()

