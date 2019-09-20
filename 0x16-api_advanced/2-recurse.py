#!/usr/bin/python3
"""
This module queries the Reddit API and and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], aft=None):
    """ This function returns the top 10 titles """
    header = {'User-Agent': 'Agenty'}
    r = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, aft)
    red_resp = requests.get(r, headers=header, allow_redirects=False)

    if red_resp.status_code >= 300:
        return None

    ret = red_resp.json().get('data').get('children')
    for e in ret:
        hot_list.append(e.get('data').get('title'))
    aft = red_resp.json().get('data').get('after')
    if aft is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, aft)
