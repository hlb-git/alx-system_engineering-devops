#!/usr/bin/python3
"""apis for reddit"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
