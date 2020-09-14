#!/usr/bin/python3
"""
    Given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    to_do = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in to_do:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(to_do)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))