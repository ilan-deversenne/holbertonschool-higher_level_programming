#!/usr/bin/python3

"""
File write
"""


def write_file(filename="", text=""):
    """
    Docstring for write_file

    :param filename: Filename
    :param text: Content to write
    """

    with open(filename, "w") as f:
        return f.write(text)
