#!/usr/bin/python3
""""doc string for the module"""


class MyList(list):
    """a class that inherits from list class"""
    def __init__(self):
        """an init method"""
        super().__init__()

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
