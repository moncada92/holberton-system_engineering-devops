#!/usr/bin/python3
'''subscribers'''


import requests


def number_of_subscribers(subreddit):
    '''get the subs'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko; Google Web Preview) \
            Chrome/27.0.1453 Safari/537.36"
    headers = {"User-Agent": agent}
    response = requests.get(url, headers=headers).json()['data']
    if response:
        return response['subscribers']
    return 0
