#!/usr/bin/python3
"""
Module containing a function that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts.
    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # A more specific, custom user-agent string avoids triggering Reddit automated drops
    headers = {"User-Agent": "ALUScripting-Task1/1.0 (by /u/NathanNduati)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
