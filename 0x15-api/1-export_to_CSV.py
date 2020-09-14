#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    to_do = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), mode='w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in to_do:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
