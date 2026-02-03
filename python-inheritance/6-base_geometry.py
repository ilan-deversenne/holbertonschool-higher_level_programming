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
