#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
print(f"{argc} arguments{":" if argc > 0 else "."}")

for i in range(1, argc + 1):
    print(f"{i}: {sys.argv[i]}")
