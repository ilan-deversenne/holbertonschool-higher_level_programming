#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = set()

    for el in set_1:
        if el not in diff and el not in set_2:
            diff.add(el)

    for el in set_2:
        if el not in diff and el not in set_1:
            diff.add(el)

    return diff
