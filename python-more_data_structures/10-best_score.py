#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    highKey, highScore = None, 0
    for key, value in a_dictionary.items():
        if value > highScore:
            highKey, highScore = key, value

    return highKey
