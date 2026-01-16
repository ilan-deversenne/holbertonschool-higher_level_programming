#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    s = "" if argc - 1 == 1 else "s"
    end = ":" if argc > 0 else "."
    print("{} argument{}{}".format(argc - 1, s, end))

    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
