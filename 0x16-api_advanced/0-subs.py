#!/usr/bin/python3
***The function retrieves the subscriber count from reddit subreddit.***
import requests

def number_of_subscribers(subreddit):
    ***return total number of subscribers from a specific subreddit.***
    url = "http://www.reddit.com/r/{}about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by u/bdov/_)"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
