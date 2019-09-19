#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress for
a given employee
"""

if __name__ == "__main__":
    import requests
    import sys

    emp_id = sys.argv[1]
    usr_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    emp_dict = requests.get(usr_url).json()
    emp_nm = emp_dict.get('name')

    td = sys.argv[1]
    td_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(td)
    td_info = requests.get(td_url).json()
    td_total = len(td_info)
    td_done = []
    for td in td_info:
        if td.get('completed'):
            td_done.append(td)
    td_count = len(td_done)
    print('Employee {} is done with tasks({}/{}):'.format(emp_nm, td_count,
                                                          td_total))
    for td in td_done:
        print('\t {}'.format(td.get('title')))
