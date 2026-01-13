#!/usr/bin/python3
c = __import__("calculator_1")

a = 10
b = 5

for op, func in {"+": c.add, "-": c.sub, "*": c.mul, "/": c.div}.items():
    print(f"{a} {op} {b} = {func(a, b)}")
