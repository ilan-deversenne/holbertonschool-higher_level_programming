#!/usr/bin/python3

"""
Check if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Docstring for is_same_class
    
    :param obj: Object to check
    :param a_class: Class to compare
    """
    return type(obj) is a_class
