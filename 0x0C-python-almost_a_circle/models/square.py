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
        return self.__size

    @size.getter
    def size(self, size):
        """size setter"""
        self.height = size
        self.width = size

    def __str__(self):
        """str method"""
        return (
            "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width, self.height
                )
            )
