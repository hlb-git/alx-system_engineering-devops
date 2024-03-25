#!/usr/bin/python3
"""Python script which makes an API call to retrieve data"""
import requests
from sys import argv


if __name__ == '__main__':
    apiUrl = "https://jsonplaceholder.typicode.com"
    taskData = requests.get("{}/todos".format(apiUrl)).json()
    userName = requests.get("{}/users/{}".format(apiUrl, argv[1])).json()
    completedTask = 0
    userTask = []
    for task in taskData:
        if (task.get("completed") is True and task["userId"] == int(argv[1])):
            completedTask += 1
        if task.get("userId") == int(argv[1]):
            userTask.append(task)
    print("Employee {} is done with tasks({}/{}):".
          format(userName.get("name"), completedTask, len(userTask)))
    for taskTitle in userTask:
        if taskTitle.get("completed") is True:
            print("\t {}".format(taskTitle.get("title")))
