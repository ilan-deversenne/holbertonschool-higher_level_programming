#!/usr/bin/python3

"""
Fetch JSONPlaceholder API
"""

import csv
import requests


def fetch_and_print_posts():
    """
    Fetch and print posts from JSONPlaceholder
    """
    result = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code: {}".format(result.status_code))
    if result.status_code == 200:
        for post in result.json():
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch and save posts from JSONPlaceholder to csv
    """
    result = requests.get("https://jsonplaceholder.typicode.com/posts")

    with open("posts.csv", 'w') as f:
        if result.status_code == 200:
            writer = csv.writer(f)
            for post in result.json():
                writer.writerow([post["id"], post["title"], post["body"]])
