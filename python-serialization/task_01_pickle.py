#!/usr/bin/env python3

"""
Docstring for python-serialization.task_01_pickle
"""


import pickle


class CustomObject:
    """
    CustomObject Class
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Docstring for __init__

        :param self: Self object
        :param name: Name
        :type name: str
        :param age: Age
        :type age: int
        :param is_student: Is student
        :type is_student: bool
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        """
        Display object data

        :param self: Self object
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename: str) -> None:
        """
        Docstring for serialize

        :param self: Self object
        :param filename: Filename
        :type filename: str
        """

        with open(filename, 'wb') as f:
            return pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename: str) -> object:
        """
        Docstring for deserialize

        :param cls: Class
        :param filename: Filename
        :type filename: str
        :return: Object
        :rtype: object
        """

        with open(filename, 'rb') as f:
            return pickle.load(f)
