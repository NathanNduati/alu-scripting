#!/usr/bin/python3
"""
Module containing a recursive function that queries the Reddit API
and returns a list containing titles of all hot articles for a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API to fetch all hot article titles.
    Returns None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUScripting/1.0 (by /u/NathanNduati)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            after_token = data.get("after")
            children = data.get("children", [])
            
            for post in children:
                hot_list.append(post.get("data", {}).get("title"))
                
            if after_token is not None:
                return recurse(subreddit, hot_list, after_token)
            return hot_list
        else:
            return None
    except Exception:
        return None
