#!/usr/bin/python3

"""
Square class
"""


class Square:
    """
        Initialize a new square instance
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    """
        Return size of square
    """
    @property
    def size(self):
        return self.__size

    """
        Set size of square
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """
        Return area of square
    """
    def area(self):
        return self.__size * self.__size

    """
        Return position of square
    """
    @property
    def position(self):
        return self.__position

    """
        Set position of square
    """
    @position.setter
    def position(self, position=(0, 0)):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    """
        Print square with #
    """
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
