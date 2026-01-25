#!/usr/bin/python3

"""
    add_integer function: Return: (int or float) add of a and b
"""

def add_integer(a, b=98):
    """
        Return: (int or float) add of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return a + b
