#!/usr/bin/python3
""" a simple doc for a simple module"""


def class_to_json(obj):
    """a function that will return the dictionary description of the obj"""
    return obj.__dict__
