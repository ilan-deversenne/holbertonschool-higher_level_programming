#!/usr/bin/python3


def main():
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, __import__("add_0").add(a, b)))


if __name__ == "__main__":
    main()
