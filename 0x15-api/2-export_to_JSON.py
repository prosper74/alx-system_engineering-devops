#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""
from sys import argv
import json
import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    USER_ID = argv[1]
    USER_URI = API_ENDPOINT + '/users/' + USER_ID
    res = requests.get(USER_URI)
    """Documentation"""
    USERNAME = res.json().get('username')
    """Documentation"""
    TODO_URI = USER_URI + '/todos'
    res = requests.get(TODO_URI)
    todos = res.json()

    dictionary_data = {USER_ID: []}
    for task in todos:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dictionary_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dictionary_data, f)
