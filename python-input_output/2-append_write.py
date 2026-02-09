#!/usr/bin/python3

"""
Append content to a file
"""


def append_write(filename="", text=""):
    """
    Docstring for append_write

    :param filename: Filename
    :param text: Content to append
    """

    with open(filename, "a") as f:
        return f.write(text)
