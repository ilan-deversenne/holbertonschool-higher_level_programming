#!/usr/bin/python3
c = __import__("calculator_1")

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, c.add(a, b)))
    print("{} - {} = {}".format(a, b, c.sub(a, b)))
    print("{} * {} = {}".format(a, b, c.mul(a, b)))
    print("{} / {} = {}".format(a, b, c.div(a, b)))
