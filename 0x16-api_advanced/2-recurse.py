#!/usr/bin/python3
'''Get ALL hot posts'''
import pprint
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    '''Get ALL hot posts'''
    headers = {'User-agent': 'API User by Wildcox80'}
    params = {'limit': 50}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    res = requests.get(BASE_URL.format(subreddit),
                       headers=headers, params=params)
    if res.status_code != 200:
        return None
    data = res.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
