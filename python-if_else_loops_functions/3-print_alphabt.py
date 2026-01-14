#!/usr/bin/python3
for letter in range(97, 122):
    if letter == 113 or letter == 101:
        continue
    print("{}".format(chr(letter)), end="")
