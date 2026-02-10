#!/usr/bin/python3
from json import dumps

"""
Convert a Class to JSON
"""


def class_to_json(obj: object) -> dict:
    """
    Docstring for class_to_json

    :param obj: Object
    """

    return obj.__dict__
