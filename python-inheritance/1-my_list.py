#!/usr/bin/python3
"""
    MyList is custom list class that inheritance from list
"""


class MyList(list):
    """
        Class init
    """
    def __init__(self):
        pass

    """
        Print sorted list
    """
    def print_sorted(self):
        print(sorted(self))
