#!/usr/bin/python3
"""
Using what you did in the task #0, extend your python script to export data in
the JSON format
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = ("{}/users/{}".format(base_url, employee_id))
    todo_url = ("{}/todos?userId={}".format(base_url, employee_id))

    # Retrieve employee information
    response = requests.get(employee_url, verify=False)
    employee_data = response.json()
    employee_name = employee_data["username"]

    # Retrieve employee's TODO list
    response = requests.get(todo_url, verify=False)
    todo_data = response.json()

    # Count total tasks and completed tasks
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task["completed"])

    # Create tasks list
    tasks = []
    for task in todo_data:
        task_data = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        }
        tasks.append(task_data)

    # Create data dictionary
    data = {
        str(employee_id): tasks
    }

    # Export data to JSON file
    filename = ("{}.json".format(employee_id))
    with open(filename, "w") as json_file:
        json.dump(data, json_file)
    print("Data exported to {} successfully.".format(filename))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
