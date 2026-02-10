#!/usr/bin/python3
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


"""
Add element(s) to add_item.json file

Usage: ./7-add_item.py [ARGS]
Usage: python3 7-add_item.py [ARGS]
"""


def main():
    """
    Entry point
    """
    if len(argv) > 1:
        argv.pop(0)
        save_to_json_file(argv, "add_item.json")


if __name__ == "__main__":
    main()
