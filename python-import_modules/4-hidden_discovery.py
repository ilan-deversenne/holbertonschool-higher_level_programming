#!/usr/bin/python3


def main():
    dirs = dir(__import__("hidden_4"))
    for d in dirs:
        if d.startswith("__"):
            continue

        print(d)


if __name__ == "__main__":
    main()
