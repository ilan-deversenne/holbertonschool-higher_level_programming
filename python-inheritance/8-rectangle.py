#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    Init BaseGeometry class
    """
    def __init__(self):
        ...

    """
    Raise Exception: area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Raise TypeError if is not int and raise ValueError if its greather that 0
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
Rectangle class
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
