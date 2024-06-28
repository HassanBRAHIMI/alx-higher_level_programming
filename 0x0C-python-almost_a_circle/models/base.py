#!/usr/bin/python3
"""the base module"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """it saves all the dictionary representations of the objs in a file"""
        with open(cls.__name__ + ".json", 'w') as labes:
            if not list_objs or len(list_objs) == 0:
                labes.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                labes.write(cls.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """it should return the pythonic way of representing a json string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            it will return an instance of the class with all
            the attributes setted
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            it returns a list of instances that have been
            created depending on the json file
        """
        file_name = cls.__name__ + '.json'
        if not os.path.isfile(file_name):
            return []
        else:
            with open(file_name, 'r') as f:
                json_str = f.read()
            f.close()
            list_of_instances_dict = cls.from_json_string(json_str)
            return [cls.create(**dict) for dict in list_of_instances_dict]
