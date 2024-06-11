#!/usr/bin/python3
""""a basic rectangle module"""


class Rectangle:
    """"the class that we will work with"""

    def __init__(self, width=0, height=0):
        """"the init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """"a getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """a setter for width"""
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """a getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """"a setter for height"""
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """"a public method to calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """"a pubilc method to calculate perimiter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
