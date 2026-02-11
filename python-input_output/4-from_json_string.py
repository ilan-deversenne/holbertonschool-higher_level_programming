#!/usr/bin/python3

"""
Parse json to an object
"""


import json


def from_json_string(my_str):
    """
    Docstring for from_json_string

    :param my_str: Json string
    """

    return json.loads(my_str)
