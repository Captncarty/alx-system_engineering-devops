#!/usr/bin/python3
""" A function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit """

import requests
import sys


def top_ten(subreddit):
    """ Queries to Reddit API """
    agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    posts = dic['data']['children']
    if len(posts) == 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
