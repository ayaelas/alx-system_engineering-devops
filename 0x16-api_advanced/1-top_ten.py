#!/usr/bin/python3
"""
Module that defines the top_ten function
"""


def top_ten(subreddit):
    """
    Queries of API
    the titles of the first 10 posts listed,
    for a given subreddit
    """
    import requests

    respond = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if respond.status_code != 200:
        print("None")
    else:
        data = respond.json().get("data")
        [print(a.get("data").get("title")) for a in data.get("children")]
