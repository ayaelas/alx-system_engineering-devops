#!/usr/bin/python3
"""
implement number_of_subscribers function
"""


def number_of_subscribers(subreddit):
    """
    Queries of API,
    Returns the num given subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "My-User-Agent"}
    respond = requests.get(url, head=headers, allow_redirects=False)

    if respond.status_code != 200:
        return 0

    return respond.json().get("data").get("subscribers")
