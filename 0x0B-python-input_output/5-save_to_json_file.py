#!/usr/bin/python3
"""a simple module"""
import json


def save_to_json_file(my_obj, filename):
    """write an obj to a json file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
