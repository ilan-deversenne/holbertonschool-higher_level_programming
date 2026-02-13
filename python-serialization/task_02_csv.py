#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename: str) -> bool:
    """
    Docstring for convert_csv_to_json

    :param filename: Filename
    :type filename: str
    :return: Success
    :rtype: bool
    """

    obj = []
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj.append(row)

    with open("data.json", 'w') as f:
        json_obj = json.dumps(obj)

        if f.write(json_obj) > 0:
            return True

    return False
