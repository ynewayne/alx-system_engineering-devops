#!/usr/bin/python3
"""Exports to-do list information for a specified employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Extract user ID from the provided command-line arguments
    user_id = sys.argv[1]

    # Base URL for the JSON API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data from the API and parse the response as JSON
    user_data = requests.get(base_url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user_data.get("username")

    # Retrieve the to-do list items associated with the user ID and parse the response as JSON
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate through the to-do list items
    # Write the details of each item (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
