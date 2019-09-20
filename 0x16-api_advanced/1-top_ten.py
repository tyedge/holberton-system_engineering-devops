#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ This function returns the top 10 titles """
    header = {'User-Agent': 'Agenty'}
    red = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    red_resp = requests.get(red, headers=header, allow_redirects=False)

    if red_resp.status_code >= 300:
        print('None')
    else:
        ret = red_resp.json().get('data').get('children')
        for r in ret:
            print(r.get('data').get('title'))
