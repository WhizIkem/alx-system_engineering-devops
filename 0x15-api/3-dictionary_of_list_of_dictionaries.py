#!/usr/bin/python3
"""
Using what you did in the task #0, extend your python script to export data in
the JSON format
"""
import json
import requests
import sys


def export_todo_all_employees():
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = ("{}/users".format(base_url))
    todo_url = ("{}/todos".format(base_url))

    # Retrieve all employees
    response = requests.get(employee_url, verify=False)
    employees = response.json()

    # Create dictionary to store tasks by employee ID
    todo_dict = {}

    # Iterate over employees
    for employee in employees:
        employee_id = employee["id"]
        employee_name = employee["username"]

        # Retrieve employee's TODO list
        response = requests.get(todo_url, params={"userId": employee_id},
                                verify=False)
        todo_data = response.json()

        # Create list to store tasks for the current employee
        tasks = []

        # Iterate over tasks
        for task in todo_data:
            task_completed_status = task["completed"]
            task_title = task["title"]

            # Create task dictionary
            task_dict = {
                "username": employee_name,
                "task": task_title,
                "completed": task_completed_status
            }

            # Append task to the list
            tasks.append(task_dict)

        # Add tasks list to the dictionary using the employee ID as the key
        todo_dict[employee_id] = tasks

    # Create JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(todo_dict, jsonfile)

    print("Data exported to {} successfully.".format(filename))


if __name__ == "__main__":
    export_todo_all_employees()
