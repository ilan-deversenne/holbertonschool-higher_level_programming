#!/usr/bin/python3

"""
    print_square (function): Print square with defined size
"""

def print_square(size):
    """
        Print square with defined size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size) # :3
