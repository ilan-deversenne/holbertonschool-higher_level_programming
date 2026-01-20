#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    highNum = 0

    for num in my_list:
        if num > highNum:
            highNum = num

    return highNum
