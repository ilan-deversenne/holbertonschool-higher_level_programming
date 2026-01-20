#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    for idx in range(length):
        num = my_list[length - idx - 1]
        print("{:d}".format(num))
