#!/usr/bin/env python3

"""
Docstring for python-serialization.task_00_basic_serialization
"""


from json import dump, load


def serialize_and_save_to_file(data: object, filename: str) -> None:
    """
    Docstring for serialize_and_save_to_file
    
    :param data: Object
    :type data: object
    :param filename: Filename
    :type filename: str
    """

    with open(filename, 'w') as f:
        dump(data, f)


def load_and_deserialize(filename: str):
    """
    Docstring for load_and_deserialize
    
    :param filename: Filename
    :type filename: str
    :return: Object
    """

    with open(filename, 'r') as f:
        return load(f)
