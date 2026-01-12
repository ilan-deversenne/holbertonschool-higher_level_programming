#!/usr/bin/python3
for i in range(9):
    for y in range(10):
        if y > i:
            print(f"{i}{y}{", " if f"{i}{y}" != "89" else "\n"}", end="")
