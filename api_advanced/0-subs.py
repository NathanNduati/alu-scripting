#!/usr/bin/python3
"""
Module containing a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the total subscriber count.
    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALUScripting/1.0 (by /u/NathanNduati)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0
    except Exception:
        return 0
