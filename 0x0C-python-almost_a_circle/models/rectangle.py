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
        for s in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """str method"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )
            )

    def update(self, *args, **kwargs):
        """a variadic method to update the instance's attributes"""
        # am a have to check the validity of args
        # then am a have to assign the attributes to a list
        # and iterate over it assigning each value to it's corresponded attr
        if args and len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    if attributes[i] == 'id':
                        self.id = arg
                    else:
                        setattr(self, attributes[i], arg)
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation"""
        empty_dic = {}
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attr in attributes:
            if hasattr(self, attr):
                empty_dic[attr] = getattr(self, attr)
        return empty_dic

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
