#!/usr/bin/python3
"""
Script to fetch todo lists of employees from an API in JSON format
Records all tasks from all employees
"""

import json
import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    USERSURI = API_ENDPOINT + "/users"

    res = requests.get(USERSURI)
    Users = res.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = '{}/users/{}'.format(API_ENDPOINT, USER_ID)
        url = url + '/todos/'
        reponse = requests.get(url)

        todos = reponse.json()
        users_dict[USER_ID] = []
        for todo in todos:
            TODO_COMPLETED = todo.get('completed')
            TODO_TITLE = todo.get('title')
            users_dict[USER_ID].append({
                "task": TODO_TITLE,
                "completed": TODO_COMPLETED,
                "username": USERNAME
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
