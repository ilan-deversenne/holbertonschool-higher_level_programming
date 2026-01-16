#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    end = ":" if argc > 0 else "."
    print("{} argument{}{}".format(argc - 1, "" if argc == 1 else "s", end))

    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
