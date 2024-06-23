#!/usr/bin/python3
"""
    creating a student class and getting it's dictionary
    representation with no filtering
"""


class Student:
    """that's a student yaaay"""
    def __init__(self, first_name, last_name, age):
        """the init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returning shit , fuck this shit"""
        return self.__dict__
