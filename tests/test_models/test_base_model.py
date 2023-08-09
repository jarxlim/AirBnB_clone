#!/usr/bin/python3
""" unittest module for the BaseModel class"""
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        '''tests the init'''
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_custom_id(self):
        '''tests the custom id'''
        custom_id = "custom_id_123"
        model = BaseModel(id=custom_id)
        self.assertEqual(model.id, custom_id)

    def test_str_representation(self):
        '''test the str representation'''
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_updates_updated_at(self):
        '''tests that storage.save() is called from save().'''
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests the public instance method to_dict()."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_updated_at_after_save(self):
        '''tests updated_at after save'''
        model = BaseModel()
        model.save()
        now = datetime.now()
        self.assertLess(model.updated_at, now)

    def test_custom_attribute(self):
        '''tests for custm attribute'''
        custom_attr_value = "custom_value"
        model = BaseModel(custom_attr=custom_attr_value)
        self.assertEqual(model.custom_attr, custom_attr_value)

    def test_to_dict_with_custom_attributes(self):
        """Tests the public instance method to_dict() with custom attr."""
        model = BaseModel()
        model.custom_attr = "custom_value"
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['custom_attr'], 'custom_value')

if __name__ == '__main__':
    unittest.main()
