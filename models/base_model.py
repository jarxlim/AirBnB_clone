#!/usr/bin/python3
"""_the main class basemodel"""

import uuid
import models
from datetime import datetime

class BaseModel():
    """class base model in which other classes inherit from"""
    def __init__(self, *args, **kwargs):
        """initialises the instant attributes

        args: the arguement lists
        kwargs: the key-value arguements
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    
    

    def __str__(self):
        """string representation of attribute

        Returns:
            official string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dic reprsentation containing all keys/values of --dict--"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict
