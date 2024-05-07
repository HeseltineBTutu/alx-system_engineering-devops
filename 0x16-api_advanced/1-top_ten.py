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
    
    if response.status_code == 404:
        print('None')

    if response.status_code == 200:
        results = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
