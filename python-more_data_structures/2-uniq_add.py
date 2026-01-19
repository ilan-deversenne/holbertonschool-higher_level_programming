#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    added = []

    for num in my_list:
        if num in added:
            continue

        added.append(num)
        result += num

    return result
