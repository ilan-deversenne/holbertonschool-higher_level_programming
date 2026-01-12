#!/usr/bin/python3
for n in range(100):
    print(f"{"0" if n < 10 else ""}{n}{", " if n < 99 else ""}", end="")
print("\n")
