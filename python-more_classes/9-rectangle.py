#!/usr/bin/python3

"""
    Rectangle class
"""


class Rectangle:
    """
        Number of instances
    """
    number_of_instances = 0

    """
        Return the bigger rectangle between rect_1 and rect_2
    """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    """
        Return new Rectangle instance with width and height == size
    """
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    """
        Initialize a new rectangle instance
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        self.print_symbol = "#"

        Rectangle.number_of_instances += 1

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

        symbol = self.print_symbol
        if isinstance(self.print_symbol, list):
            symbol = self.print_symbol[0]

        for i in range(self.__height):
            result += symbol * self.__width

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
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
