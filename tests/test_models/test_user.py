import unittest
from models.user import User
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage

class TestUserModel(unittest.TestCase):

    def setUp(self):
        """Sets up test methods."""
        self.user_data = {
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe"
        }
        self.user = User(**self.user_data)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_user_str_representation(self):
        """Test if the __str__ method produces the expected string representation."""
        expected_str = f"[User] ({self.user.id}) {str(self.user.__dict__)}"
        self.assertEqual(str(self.user), expected_str)

    def test_user_attributes(self):
        """Tests the attributes of User class."""
        attributes = self.user_data.keys()
        o = User()
        for k in attributes:
                self.assertTrue(hasattr(o, k))
                self.assertEqual(getattr(o, k, None), "")

if __name__ == '__main__':
    unittest.main()
