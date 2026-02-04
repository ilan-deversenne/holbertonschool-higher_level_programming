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
    """
    Init rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    """
    Area of rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
    Return string
    """
    def __str__(self):
        name = self.__class__.__name__
        return "[{}] {}/{}".format(name, self.__width, self.__height)


"""
Square class
"""


class Square(Rectangle):
    """
    Init square
    """
    def __init__(self, size):
        super().__init__(size, size)

        self.__size = size
        self.integer_validator("size", size)
