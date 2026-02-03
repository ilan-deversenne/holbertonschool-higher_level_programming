#!/usr/bin/env python3

"""
CountedIterator class
"""


class CountedIterator():
    """
    Init CountedIterator
    """
    def __init__(self, interator):
        super().__init__()

        self.__counter = 0
        self.__iterrator = iter(interator)

    """
    Return count of iteration
    """
    def get_count(self):
        return self.__counter

    """
    Override next to increment counter
    """
    def __next__(self):
        self.__counter += 1
        return next(self.__iterrator)
