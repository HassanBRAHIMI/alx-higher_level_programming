#!/usr/bin/python3
"""
    a square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """an update method"""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i, attr in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == 'id':
                        self.id = attr
                    else:
                        setattr(self, attrs[i], attr)
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation"""
        empty_dic = {}
        attributes = ['id', 'size', 'x', 'y']
        for attr in attributes:
            if hasattr(self, attr):
                empty_dic[attr] = getattr(self, attr)
        return empty_dic

    def __str__(self):
        """str method"""
        return (
            "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width, self.height
                )
            )
