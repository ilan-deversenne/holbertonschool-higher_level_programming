#!/usr/bin/python3

"""
Convert json file content to a object
"""


from json import load


def load_from_json_file(filename):
    """
    Docstring for load_from_json_file

    :param filename: Filename
    """

    with open(filename, 'r') as f:
        return load(f)
