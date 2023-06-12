#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = ("{}/users/{}".format(base_url, employee_id))
    todo_url = ("{}/todos?userId={}".format(base_url, employee_id))

    # Retrieve employee information
    response = requests.get(employee_url, verify=False)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Retrieve employee's TODO list
    response = requests.get(todo_url, verify=False)
    todo_data = response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    # Display progress
    progress_status = "{}/{}".format(done_tasks, total_tasks)
    # progress_status = "OK" if done_tasks == total_tasks else "Incorrect"
    print("Employee {} is done with tasks ({}/{}):".format(employee_name,
          done_tasks, total_tasks))

    # Display completed task titles
    for task in todo_data:
        if task['completed']:
            print("\t", task['title'])

# Example usage: provide the employee ID as a command-line argument


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
