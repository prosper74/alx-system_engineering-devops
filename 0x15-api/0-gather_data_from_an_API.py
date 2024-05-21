#!/usr/bin/python3
"""
Script that returns information about a user TODO list progress.,
using this REST API, for a given employee ID
"""

import re
import requests
from sys import argv

API_ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            id = int(argv[1])
            req = requests.get('{}/users/{}'.format(API_ENDPOINT, id)).json()
            todo_req = requests.get('{}/todos'.format(API_ENDPOINT)).json()
            user_name = req.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todo_req))
            completed_todos = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(completed_todos),
                    len(todos)
                )
            )
            if len(completed_todos) > 0:
                for todo in completed_todos:
                    print('\t {}'.format(todo.get('title')))
