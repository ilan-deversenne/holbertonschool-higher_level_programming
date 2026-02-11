#!/usr/bin/python3

"""
Convert a Class to JSON
"""


from json import dumps


def class_to_json(obj: object) -> dict:
    """
    Docstring for class_to_json

    :param obj: Object
    """

    return obj.__dict__
