#!/usr/bin/python3
"""Defines for the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """class represent a city.

    Attributes:
        state_id (str): state id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
