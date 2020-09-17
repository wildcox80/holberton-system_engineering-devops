#!/usr/bin/python3
'''Get top 10 hot posts'''
import pprint
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''Get top 10 hot posts'''
    headers = {'User-agent': 'API User by Wildcox80'}
    res = requests.get(BASE_URL.format(subreddit),
                       headers=headers)
    data = res.json().get('data', {}).get('children', {})
    if res.status_code != 200 or not data:
        return print("None")
    for post in data[0:10]:
        print(post.get('data', {}).get('title'))
