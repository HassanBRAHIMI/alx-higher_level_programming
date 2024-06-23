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

    def to_json(self, attrs=None):
        """returning shit , fuck this shit"""
        if attrs is None:
            return self.__dict__
        emty_dic = {}
        for attr in attrs:
            if hasattr(self, attr):
                emty_dic[attr] = getattr(self, attr)
        return emty_dic
