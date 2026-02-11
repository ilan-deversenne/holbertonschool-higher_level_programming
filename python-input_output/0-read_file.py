#!/usr/bin/python3

"""
Print content of file with his filename
"""


def read_file(filename=""):
    """
    Docstring for read_file

    :param filename: Filename
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
