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
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        Filestorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        seri_obj = {key: FileStorage.__objects[key].to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(seri_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON FILE)"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, obj_dict in objects_dict.items():
                    class_name = obj_dict['__class__']
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
