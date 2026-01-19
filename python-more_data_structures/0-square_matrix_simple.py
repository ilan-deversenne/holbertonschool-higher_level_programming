#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for x in matrix:
        el = []
        for y in x:
            el.append(y * y)

        new_matrix.append(el)

    return new_matrix
