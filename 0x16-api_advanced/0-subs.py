#!/usr/bin/python3
"""This module queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """ This function returns the number of subscribers """
    header = {'User-Agent': 'Agenty'}
    red_resp = requests.get('https://www.reddit.com/r/{}/about.\
    json'.format(subreddit), headers=header, allow_redirects=False)

    if red_resp.status_code > 300:
        return 0
    return (red_resp.json().get('data').get('subscribers'))
