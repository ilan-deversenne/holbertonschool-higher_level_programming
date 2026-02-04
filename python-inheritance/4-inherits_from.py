#!/usr/bin/python3

"""
Check if the object is an instance of a class that inherited from given class
"""


def inherits_from(obj, a_class):
    """
    Docstring for inherits_from
    
    :param obj: Object
    :param a_class: Class to compare
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
