#!/usr/bin/env python3
from math import pi
from abc import ABC, abstractmethod

"""
Shape class
"""


class Shape(ABC):
    """
    Init Shape
    """
    def __init__(self):
        super().__init__()

    """
    return Area
    """
    @abstractmethod
    def area(self):
        pass

    """
    Return perimeter
    """
    @abstractmethod
    def perimeter(self):
        pass


"""
Circle class
"""


class Circle(Shape):
    """
    Init Circle
    """
    def __init__(self, radius):
        super().__init__()

        self.__radius = radius

    """
    Return Area
    """
    def area(self):
        return pi * (self.__radius * self.__radius)

    """
    Return perimeter
    """
    def perimeter(self):
        return 2 * pi * self.__radius


"""
Rectangle class
"""


class Rectangle(Shape):
    """
    Init Rectangle
    """
    def __init__(self, width, height):
        super().__init__()

        self.__width = width
        self.__height = height

    """
    Return Area
    """
    def area(self):
        return self.__width * self.__height

    """
    Return perimeter
    """
    def perimeter(self):
        return (2 * self.__height) + (2 * self.__width)


"""
Print shape info (area, perimeter)
"""
def shape_info(obj: Shape):
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
