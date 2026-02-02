#!/usr/bin/python3
"""
Check if the object is an instance of a class that inherited from given class
"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) != a_class
