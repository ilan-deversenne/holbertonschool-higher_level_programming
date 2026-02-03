#!/usr/bin/env python3

"""
Fish class
"""


class Fish:
    """
    Init Fish
    """
    def __init__(self):
        pass

    """
    Swim
    """
    def swim(self):
        print("The fish is swimming")

    """
    Print habitat of Fish
    """
    def habitat(self):
        print("The fish lives in water")


"""
Bird class
"""


class Bird:
    """
    Init Bird
    """
    def __init__(self):
        pass

    """
    Fly
    """
    def fly(self):
        print("The bird is flying")

    """
    Print habitat of bird
    """
    def habitat(self):
        print("The bird lives in the sky")


"""
FlyingFish class
"""


class FlyingFish(Fish, Bird):
    """
    Init FlyingFish
    """
    def __init__(self):
        super().__init__()

    """
    Fly
    """
    def fly(self):
        print("The flying fish is soaring!")

    """
    Swim
    """
    def swim(self):
        print("The flying fish is swimming!")

    """
    Print habitat of FlyingFish
    """
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
