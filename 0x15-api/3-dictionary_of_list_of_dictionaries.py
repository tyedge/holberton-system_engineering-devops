#!/usr/bin/python3
"""
This module uses the REST API and, for a given employee ID, returns information
about his/her TODO list progress and exports that data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    usr_url = 'https://jsonplaceholder.typicode.com/users'
    emp_dict = requests.get(usr_url).json()
    tds = {}
    for emp in emp_dict:
        emp_id = str(emp.get('id'))
        tds[emp_id] = []
        td_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.\
                 format(emp_id)
        td_info = requests.get(td_url).json()
        for td in td_info:
            info = {"username": emp.get('username'), "task": td.get('title'),
                    "completed": td.get('completed')}
            tds[emp_id].append(info)
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(tds, file)
