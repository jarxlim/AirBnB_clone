#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test for the City class."""

    def setUp(self):
        """sets test methods up."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_city_attributes(self):
        """Tests the attributes of City class."""
        o = City()
        attributes = ["id", "created_at", "updated_at", "name", "state_id"]
        for attr in attributes:
            self.assertTrue(hasattr(o, attr))

if __name__ == "__main__":
    unittest.main()
