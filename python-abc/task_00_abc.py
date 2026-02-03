#!/usr/bin/env python3
from abc import ABC, abstractmethod

"""
Animal class
"""


class Animal(ABC):
    """
    Init animal
    """
    def __init__(self):
        super().__init__()

    """
    Return string of animal sound
    """
    @abstractmethod
    def sound(self):
        pass


"""
Dog class
"""


class Dog(Animal):
    """
    Init dog
    """
    def __init__(self):
        super().__init__()

    """
    Return string of animal sound
    """
    def sound(self):
        return "Bark"


"""
Cat class
"""


class Cat(Animal):
    """
    Init cat
    """
    def __init__(self):
        super().__init__()

    """
    Return string of animal sound
    """
    def sound(self):
        return "Meow"
