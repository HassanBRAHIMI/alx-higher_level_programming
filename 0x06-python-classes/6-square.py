#!/usr/bin/python3
"""creating a simple class"""


class Square:
    """""square class"""

    def __init__(self, size=0, position=(0, 0)):
        """"defining attrib size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of the class"""
        return self.__position

    @position.setter
    def position(self, position):
        """setter of the position in the class"""
        if (not isinstance(position, tuple) or
            not all(isinstance(num, int) for num in position)
            or not all(value >= 0 for value in position)
                or len(position) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            for k in range(self.__position[0]):
                print(" ", end="")
            while j < self.__size:
                print("#", end="")
                j += 1
            print("")
            i += 1
