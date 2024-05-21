#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""

from sys import argv
import csv
import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    USER = argv[1]
    USERNAME = API_ENDPOINT + '/users/' + USER
    res = requests.get(USERNAME)
    """ANYTHING"""
    user_name = res.json().get('username')
    TODO_URI = USERNAME + '/todos'
    res = requests.get(TODO_URI)
    tasks = res.json()

    with open('{}.csv'.format(USER), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                USER, user_name, completed, title_task))
