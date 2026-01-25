#!/usr/bin/python3

"""
    matrix_divided function: Divide a matrix
"""

def matrix_divided(matrix, div):
    """
        Return: (list) matrix divided by div
    """

    result = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    first_len = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for arr in matrix:
        if not isinstance(arr, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(arr) != first_len:
            raise TypeError("Each row of the matrix must have the same size")

        child = []

        for el in arr:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            child.append(round(el / div, 2))
        result.append(child)

    return result
