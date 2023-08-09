#!/usrbin/python3
"""file storage to be reopened later"""
import json
from os.path import exists
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
        seri_obj = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(seri_obj, fl)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON FILE)"""
        try:
            with open(FileStorage.__file_path) as fl:
                seri_obj = json.load(fl)
                for key in seri_obj.values():
                    class_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(class_name)(**key))
        except FileNotFoundError:
            return
