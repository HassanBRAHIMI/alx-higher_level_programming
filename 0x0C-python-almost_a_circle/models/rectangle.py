#!/usr/bin/python3
from base import Base
"""a rectangle module"""


class Rectangle(Base):
    """a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    