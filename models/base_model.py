#!/usr/bin/python3
"""_the main class basemodel"""

import uuid
import cmd
from datetime import datetime

class BaseModel():
    """class base model
    """
    def __init__(self, *args, **kwargs):
        """init: instantiation
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ['create_at, updated_at']:
                    self.__dict__[k] = datetime.strptime(v, '%y-%m-%dT%H:&M:%S.%f')
                else:
                    self.__dict__[k] = v
        
    def __str__(self):
        """string representation of attribute

        Returns:
            str: string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """to update the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """dic reprsentation

        Returns:
            dic: to make them suitable for serialisation
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['created_at'] = self.created_at.isoformat()
        
        return obj_dict
