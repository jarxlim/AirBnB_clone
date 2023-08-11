import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Sets up test methods."""
        self.storage = FileStorage()

    def test_new_object_added(self):
        '''tests for new objects added'''
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage.all())

    def test_new_object_not_added_with_existing_id(self):
        '''test for new object not added id'''
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        original_objects = self.storage.all().copy()
        self.storage.new(obj)

        self.assertEqual(self.storage.all(), original_objects)

    def test_save_and_reload(self):
        '''test for save and reload'''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, new_storage.all())

    def test_save_empty_storage(self):
        ''' Should not raise an exception'''
        self.storage.save()

    def test_reload_non_existing_file(self):
        '''Should not raise an exception'''
        non_existing_storage = FileStorage()
        non_existing_storage.reload()

    def test_reload_existing_file(self):
        '''tests for reloading existing file'''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        reloaded_storage = FileStorage()
        reloaded_storage.reload()

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, reloaded_storage.all())

    def test_all_non_empty_storage(self):
        ''' tests for all non empty storage'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_objects = self.storage.all()
        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

    def test_new_object_type(self):
        ''' test for new object type'''
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        stored_obj = self.storage.all()[obj_key]
        self.assertIsInstance(stored_obj, BaseModel)

    def test_save_with_custom_attributes(self):
        '''test for save with custom attributes'''
        obj = BaseModel()
        obj.custom_attr = "custom_value"
        self.storage.new(obj)
        self.storage.save()

        reloaded_storage = FileStorage()
        reloaded_storage.reload()

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        reloaded_obj = reloaded_storage.all()[obj_key]
        self.assertEqual(reloaded_obj.custom_attr, "custom_value")

    def test_save_and_reload_multiple_objects(self):
        '''test save and reload objs'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()

        reloaded_storage = FileStorage()
        reloaded_storage.reload()

        obj1_key = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        obj2_key = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        obj3_key = "{}.{}".format(obj3.__class__.__name__, obj3.id)
        self.assertIn(obj1_key, reloaded_storage.all())
        self.assertIn(obj2_key, reloaded_storage.all())
        self.assertIn(obj3_key, reloaded_storage.all())

if __name__ == '__main__':
    unittest.main()
