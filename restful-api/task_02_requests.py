#!/usr/bin/python3

"""
Fetch JSONPlaceholder API
"""

import requests


def fetch_and_print_posts():
    """
    Fetch and print posts from JSONPlaceholder
    """
    result = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code: {}".format(result.status_code))
    if result.status_code == 200:
        print(result.json())


fetch_and_print_posts()
