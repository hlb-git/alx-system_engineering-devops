#!/usr/bin/python3
""" Export api response data to csv"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user).json()
    user_name = res.get('username')
    task = url_user + '/todos'
    res = requests.get(task).json()
    tasks = res

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')  # Complete
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
