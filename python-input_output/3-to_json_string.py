#!/usr/bin/python3
import json

"""
Object to json string
"""


def to_json_string(my_obj):
    """
    Docstring for to_json_string

    :param my_obj: Object
    :type my_obj: object
    :return: JSON String representation of my_obj
    :rtype: str
    """

    return json.dumps(my_obj)
