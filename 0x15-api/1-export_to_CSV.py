#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress for
a given employee
"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

    emp_id = sys.argv[1]
    usr_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    emp_dict = requests.get(usr_url).json()
    emp_nm = emp_dict.get('name')
    uname = emp_dict.get('username')
    uid = emp_dict.get('id')
    td = sys.argv[1]
    td_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(td)
    td_info = requests.get(td_url).json()
    with open(emp_id + '.csv', mode='w') as file:
        ret = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL,
                         quotechar='"')
        for td in td_info:
            ret.writerow((uid, uname, td.get('completed'), td.get('title')))
