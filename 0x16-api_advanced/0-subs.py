#!/usr/bin/python3
"""
Returns number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """return nmber of subscribers given"""
    base_url = "https://www.reddit.com/r/{}/about.json"
    
    
    headers = {
        "User-Agent": "MySubredditInfoApp/1.0 (by /u/ayaelas)"
    }
    
    url = base_url.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
        
    if response.status_code == 200:
       data = response.json()
       subscribers = data['data']['subscribers']
       return subscribers
    return 0
