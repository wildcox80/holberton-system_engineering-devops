#!/usr/bin/python3
"""
    Given employee ID, returns information about his/her TODO list progress.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    API_URL = "https://jsonplaceholder.typicode.com/"
    people = requests.get(API_URL + "users/" + argv[1])
    to_do = requests.get(API_URL + "todos?userId=" + argv[1])
    name = people.json().get("name")
    tasks = len(to_do.json())
    done = 0

    for task in to_do.json():
        if task.get("completed"):
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))

    for task in to_do.json():
        if task.get("completed"):
            print("\t ", end="")
            print(task.get("title"))
