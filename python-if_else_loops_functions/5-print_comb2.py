#!/usr/bin/python3
for n in range(100):
    start = "0" if n < 10 else ""
    print("{}{}{}".format(start, n, ", " if n < 99 else ""), end="")

print("")
