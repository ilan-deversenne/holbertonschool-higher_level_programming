#!/usr/bin/python3
c = __import__("calculator_1")

if __name__ == "__main__":
    a = 10
    b = 5

    for op, func in {"+": c.add, "-": c.sub, "*": c.mul, "/": c.div}.items():
        print("{} {} {} = {}".format(a, op, b, func(a, b)))
