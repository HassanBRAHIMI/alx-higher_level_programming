#!/usr/bin/python3
"""a simple module"""


def inherits_from(obj, a_class):
    """
        checks if an object is an instance
        of a class that inherited from the a_class
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
