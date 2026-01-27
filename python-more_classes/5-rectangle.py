#!/usr/bin/python3

"""
    Rectangle class
"""


class Rectangle:
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

    """
        Return the area of the rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
        Return the perimeter of the rectangle
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    """
        Return a rectangle with defined width and height
    """
    def __str__(self):
        result = ""

        for i in range(self.__height):
            result += "#" * self.__width

            if i < self.__height - 1:
                result += "\n"

        return result

    """
        Return a string representation of the object that can be evaluated
    """
    def __repr__(self):
        name = self.__class__.__name__
        w, h = self.__width, self.__height

        return f"{name}({w}, {h})"

    """
        Print "Bye rectangle..." when class is deleted
    """
    def __del__(self):
        print("Bye rectangle...")
