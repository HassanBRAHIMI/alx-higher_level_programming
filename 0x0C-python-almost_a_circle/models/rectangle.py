#!/usr/bin/python3
"""
    a rectangle module
"""
from models.base import Base


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
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for the width"""
        self.__width = width

    @property
    def height(self):
        """getter of the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of the height"""
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
