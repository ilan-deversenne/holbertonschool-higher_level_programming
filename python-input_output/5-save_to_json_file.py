#!/usr/bin/python3
from json import dump

"""
Save object to a json file
"""


def save_to_json_file(my_obj, filename):
    """
    Docstring for save_to_json_file

    :param my_obj: Object
    :param filename: Filename
    """

    print(filename, my_obj)

    with open(filename, "w") as f:
        dump(list(my_obj), f)
