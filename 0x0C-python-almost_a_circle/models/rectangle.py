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
        self.setter_validation(width, "width")
        self.__width = width

    @property
    def height(self):
        """getter of the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of the height"""
        self.setter_validation(height, "height")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.setter_validation(x, "x")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.setter_validation(y, "y")
        self.__y = y

    def area(self):
        """an area method"""
        return (self.__height * self.__width)

    def display(self):
        """display method"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """str method"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )
            )

    @staticmethod
    def setter_validation(value, name_of_the_attr):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name_of_the_attr))
        elif name_of_the_attr == "x" or name_of_the_attr == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name_of_the_attr))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name_of_the_attr))
