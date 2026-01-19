#!/usr/bin/python3

def max_integer(my_list=[]):
    highNum = 0

    for num in my_list:
        if num > highNum:
            highNum = num

    return highNum
