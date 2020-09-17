#!/usr/bin/python3
'''Get number of reddit channel subscribers'''
import requests

BASE_URL = 'http://reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    '''Gets number of reddit subscribers'''
    headers = {'User-agent': 'API User by Wildcox80'}
    res = requests.get(BASE_URL.format(subreddit),
                       headers=headers)
    if res.status_code != 200:
        return 0
    return res.json().get('data', {}).get('subscribers', 0)
