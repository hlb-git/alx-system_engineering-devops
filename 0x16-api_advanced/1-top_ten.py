#!/usr/bin/python3
"""top 10 hot posts"""
import requests
from sys import argv


def top_ten(subreddit):
    '''returns the top ten posts for a subreddit'''
    user = {'User-Agent': 'Mozilla/5.0'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
