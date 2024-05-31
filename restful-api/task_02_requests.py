#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
            