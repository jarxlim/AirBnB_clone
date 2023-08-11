#!usr/bin/python3
"""module for creating users"""
from models.base_model import BaseModel


class User(BaseModel):
    """for creating user's profile

    Attributes:
        email (str): The email address of the user.
        password (str): The security code of the user.
        first_name (str): The person's firstname
        last_name (str): father's name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
