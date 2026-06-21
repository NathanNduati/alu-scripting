#!/usr/bin/python3
"""
Module containing a recursive function that queries the Reddit API,
parses hot article titles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively queries the Reddit API, counts occurrences of keywords
    in hot article titles, and prints them sorted by count (descending)
    and alphabetically (ascending).
    """
    if not counts:
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUScripting/1.0 (by /u/NathanNduati)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        after_token = data.get("after")
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            # Split by space to check for strict space-delimited keyword matches
            words_in_title = title.split()
            for word in words_in_title:
                # Strip common ending punctuations to extract clean words
                cleaned_word = word.strip(".,?!_")
                if cleaned_word in counts:
                    counts[cleaned_word] += 1

        if after_token is not None:
            return count_words(subreddit, word_list, after_token, counts)

        # Base case reached: Sort and print results
        # Sort key: count descending (-x[1]), then word alphabetically ascending (x[0])
        sorted_counts = sorted(
            [item for item in counts.items() if item[1] > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return
