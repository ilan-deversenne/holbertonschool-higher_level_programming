#!/usr/bin/python3
from json import loads

"""
Parse json to an object
"""


def from_json_string(my_str):
    """
    Docstring for from_json_string

    :param my_str: Json string
    """

    return loads(my_str)
