#!/usr/bin/python3
for i in range(9):
    for y in range(10):
        if y > i:
            end = ", " if f"{i}{y}" != "89" else "\n"
            print("{}{}{}".format(i, y, end), end="")
