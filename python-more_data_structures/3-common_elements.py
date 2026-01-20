#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = set()

    for idx, el in enumerate(set_1):
        if idx > len(set_2):
            break

        if el in set_2:
            common.add(el)

    return common
