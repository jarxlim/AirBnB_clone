#!/usrbin/python3
"""file storage to be reopened later"""
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """the file storage class

    Attributes:
        __file_path (str): the saved file name
        __objects (dict): objects in a dictionary type format.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dd = FileStorage.__objects
        seri_obj = {obj: dd[obj].to_dict() for obj in dd.keys()}
        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(seri_obj, fl)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON FILE)"""
        try:
            with open(FileStorage.__file_path) as fl:
                seri_obj = json.load(fl)
                for key in seri_obj.values():
                    cls_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
