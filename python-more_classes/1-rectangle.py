#!/usr/bin/python3

"""
    Rectangle class
"""


class Rectangle:
    """
        Initialize a new rectangle instance
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """
        Return width of the rectangle
    """
    @property
    def width(self):
        return self.__width

    """
        Set rectangle width
    """
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    """
        Return height of the rectangle
    """
    @property
    def height(self):
        return self.__height

    """
        Set rectangle height
    """
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
