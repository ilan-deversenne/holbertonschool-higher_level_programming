#!/usr/bin/python3

def pascal_triangle(n: int) -> list:
    """
    Docstring for pascal_triangle

    :param n: Number of desired columns
    :type n: int
    :return: List with all columns
    :rtype: list
    """

    column = []

    for x in range(n):
        row = [1]

        if len(column) > 0:
            for y in range(1, len(column[x - 1])):
                row.append(column[x - 1][y] + column[x - 1][y - 1])

            row.append(1)
        column.append(row)

    return column
