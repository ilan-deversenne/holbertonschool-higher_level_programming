#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for y in x:
            i += 1
            print("{}{}".format(y, " " if i < len(x) else ""), end="")
        print("")
