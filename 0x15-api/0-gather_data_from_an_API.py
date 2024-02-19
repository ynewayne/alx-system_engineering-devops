#!/usr/bin/python3
"""
Retrieves to-do list information for a specified employee ID.

This script accepts an employee ID as a command-line argument and retrieves
the corresponding user information and to-do list from the JSONPlaceholder API.
It then displays the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee information using the provided employee ID
    employee_id = sys.argv[1]
    user_info = requests.get(api_url + "users/{}".format(employee_id)).json()

    # Obtain the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todo_list = requests.get(api_url + "todos", params).json()

    # Identify completed tasks and count them
    completed_tasks = [task.get("title") for task in todo_list if task.get("completed")]

    # Display the employee's name and the count of completed tasks
    print("Employee {} has completed the following tasks ({}/{}):".format(
        user_info.get("name"), len(completed_tasks), len(todo_list)))

    # Display completed tasks one by one with appropriate indentation
    [print("\t{}".format(task)) for task in completed_tasks]
