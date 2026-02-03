#!/usr/bin/env python3

"""
SwimMixin class
"""


class SwimMixin:
    """
    Init SwimMixin
    """
    def __init__(self):
        pass

    """
    Swim
    """
    def swim(self):
        print("The creature swims!")


"""
FlyMixin class
"""


class FlyMixin:
    """
    Init FlyMixin
    """
    def __init__(self):
        pass

    """
    Fly
    """
    def fly(self):
        print("The creature flies!")


"""
Dragon class
"""


class Dragon(SwimMixin, FlyMixin):
    """
    Init Dragon
    """
    def __init__(self):
        pass

    """
    Roar
    """
    def roar(self):
        print("The dragon roars!")
