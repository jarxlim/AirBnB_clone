#!usr/bin/python3
"""creating users"""
from models.base_model import BaseModel


class User(BaseModel):
    """for creating users profile

    Attributes:
        email (str): The email address of the user.
        password (str): The security code of the user.
        first_name (str): The person's name of the user.
        last_name (str): father's name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
