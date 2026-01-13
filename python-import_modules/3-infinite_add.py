#!/usr/bin/python3
import sys


def main():
    result = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            num = int(sys.argv[i])
            result += num

    print(result)


if __name__ == "__main__":
    main()
