#!/usr/bin/python3

"""
Student class
"""


class Student:
    """
    Init students class
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Docstring for __init__

        :param self: Self object
        :param first_name: First name
        :type first_name: str
        :param last_name: Last name
        :type last_name: str
        :param age: Age
        :type age: int
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: list = None) -> dict:
        """
        Docstring for to_json

        :param self: Self object
        :param attrs: Filter
        :type attrs: list
        :return: Json list
        :rtype: dict
        """
        result = {}

        if type(attrs) is list and len(attrs) > 0:
            for el in attrs:
                if el in self.__dict__:
                    result[el] = self.__dict__[el]
        else:
            result = self.__dict__

        return result

    """
    Reload from JSON
    """
    def reload_from_json(self, json: dict):
        """
        Docstring for reload_from_json

        :param self: Self object
        :param json: Class JSON object
        :type json: dict
        """

        for key, value in json.items():
            self.__dict__[key] = value
