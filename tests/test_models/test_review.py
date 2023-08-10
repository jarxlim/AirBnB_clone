#!/usr/bin/python3
"""Unittest module for testing the Review class."""

import unittest
from models.review import Review
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

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
        """Test instantiation of the Review class."""
        review_obj = Review()
        self.assertEqual(str(type(review_obj)), "<class 'models.review.Review'>")
        self.assertIsInstance(review_obj, Review)
        self.assertTrue(issubclass(type(review_obj), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Review class."""
        review_obj = Review()
        attributes = ["id", "created_at", "updated_at", "place_id", "user_id", "text"]
        for attr in attributes:
            self.assertTrue(hasattr(review_obj, attr))
            
if __name__ == "__main__":
    unittest.main()

