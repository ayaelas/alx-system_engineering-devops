#!/usr/bin/python3
"""
Returns number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """return nmber of subscribers given"""
    base_url = "https://www.reddit.com/r/{}/about.json"
    
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    # Format the URL with the subreddit name
    url = base_url.format(subreddit)
    
    response = requests.get(url, headers=headers, allow_redirects=False)
        
    if response.status_code == 200:
       data = response.json()
       subscribers = data['data']['subscribers']
       return subscribers
    return 0
