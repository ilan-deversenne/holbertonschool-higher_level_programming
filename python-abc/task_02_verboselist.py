#!/usr/bin/env python3

"""
VerboseList class
"""


class VerboseList(list):
    """
    Init VerboseList
    """
    def __init__(self, iterable):
        super().__init__(iterable)

    """
    Override to print message after append
    """
    def append(self, object):
        result = super().append(object)
        print("Added [{}] to the list.".format(object))

        return result

    """
    Override to print message after extend
    """
    def extend(self, iterable):
        result = super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

        return result

    """
    Override to print message after remove
    """
    def remove(self, value):
        result = super().remove(value)
        print("Removed [{}] from the list.".format(value))

        return result

    """
    Override to print message after pop
    """
    def pop(self, index=-1):
        value = self[index]
        result = super().pop(index)

        print("Popped [{}] from the list.".format(value))

        return result
