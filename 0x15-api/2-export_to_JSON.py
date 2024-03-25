#!/usr/bin/python3
""" export API response to Json"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user).json()
    USERNAME = res.get('username')
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task).json()
    tasks = res

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    with open('{}.json'.format(USER_ID), 'w') as file:
        json.dump(dict_data, file)
