#!/usr/bin/python3
result = ""

for n in range(99):
    result += f"{n} = {hex(n)}{"\n" if n < 98 else ""}"

print(result)
