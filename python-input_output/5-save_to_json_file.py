#!/usr/bin/python3
"""
Save object to a json file
"""


from json import dump


def save_to_json_file(my_obj, filename):
    """
    Docstring for save_to_json_file

    :param my_obj: Object
    :param filename: Filename
    """

    with open(filename, "w") as f:
        dump(my_obj, f, default=lambda x:"")
