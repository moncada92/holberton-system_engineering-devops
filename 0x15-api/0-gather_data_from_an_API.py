#!/usr/bin/python3
"""reques API"""

import requests
from sys import argv


def getData(id):
    '''get data of employee'''
    URL = 'https://jsonplaceholder.typicode.com/'
    ENDPOINT = URL + 'users/{}'.format(id)
    employee = requests.get(ENDPOINT).json()
    TASKENDPOINT = URL + 'todos?userId={}'.format(employee.get('id'))
    tasks = requests.get(TASKENDPOINT).json()
    data = {"employee": employee, "tasks": tasks}
    total = len(data['tasks'])
    tasks = [task for task in data['tasks'] if task['completed']]
    completed = len(tasks)
    print('Employee {} is done with tasks({}/{}):'
          .format(data['employee']['name'], completed, total))
    for task in tasks:
        print('\t {}'.format(task['title']))


if __name__ == '__main__':
    getData(argv[1])
