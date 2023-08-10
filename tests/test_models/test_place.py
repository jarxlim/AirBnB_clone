#!/usr/bin/python3
"""Unittest module for testing the Place class."""

import unittest
from models.place import Place
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

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
        """Test instantiation of the Place class."""
        place_obj = Place()
        self.assertEqual(str(type(place_obj)), "<class 'models.place.Place'>")
        self.assertIsInstance(place_obj, Place)
        self.assertTrue(issubclass(type(place_obj), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Place class."""
        place_obj = Place()
        attributes = ["id", "created_at", "updated_at", "city_id", "user_id", "name", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude", "amenity_ids"]
        for attr in attributes:
            self.assertTrue(hasattr(place_obj, attr))
            
if __name__ == "__main__":
    unittest.main()

