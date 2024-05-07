#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

    if not posts:
        return
    for post in posts[:10]:
        print(post["data"]["title"])
