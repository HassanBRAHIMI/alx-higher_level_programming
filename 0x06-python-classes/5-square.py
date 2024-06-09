#!/usr/bin/python3
"""creating a simple class"""


class Square:
    """""square class"""

    def __init__(self, size):
        """"defining attrib size"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """"getter of the class"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter of the class"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """"calculate the are of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
            return
        i = 0
        j = 0
        while i < self.__size:
            j = 0
            while j < self.__size:
                print("#", end="")
                j += 1
            print("")
            i += 1
