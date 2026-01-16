#!/usr/bin/python3
import sys

argc = len(sys.argv)
print("{} arguments{}".format(argc - 1, ":" if argc > 0 else "."))

for i in range(1, argc):
    print("{}: {}".format(i, sys.argv[i]))
