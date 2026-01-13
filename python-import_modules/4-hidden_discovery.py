#!/usr/bin/python3
__import__("hidden_4")


def main():
    dirs = dir()
    for d in dirs:
        if d.startswith("__"):
            continue

        print(d)


if __name__ == "__main__":
    main()
