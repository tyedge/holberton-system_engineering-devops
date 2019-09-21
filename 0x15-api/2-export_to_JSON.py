#!/usr/bin/python3
"""
This module uses the REST API and, for a given employee ID, returns information
about his/her TODO list progress and exports that data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    emp_id = sys.argv[1]
    usr_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    emp_dict = requests.get(usr_url).json()
    emp_nm = emp_dict.get('name')

    td = sys.argv[1]
    td_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(td)
    td_info = requests.get(td_url).json()
    tds = []
    for td in td_info:
        add_info = {"task": td.get('title'), "completed": td.get('completed'),
                    "username": emp_dict.get('username')}
        tds.append(add_info)
    main_dict = {'{}'.format(emp_id): tds}

    with open('{}.json'.format(emp_id), mode='w') as file:
        json.dump(main_dict, file)
