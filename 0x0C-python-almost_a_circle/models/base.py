#!/usr/bin/python3
"""the base module"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
