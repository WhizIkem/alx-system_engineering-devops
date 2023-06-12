#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(base_url, employee_id)
    todos_url = '{}/todos?userId={}'.format(base_url, employee_id)

    # Fetch employee information
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Error: Could not retrieve employee information. Status code: {}".format(employee_response.status_code))
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Could not retrieve TODO list. Status code: {}".format(todos_response.status_code))
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    # Display progress information
    print("Employee {} is done with tasks ({}/{}):".format(employee_name,
          num_completed_tasks, total_tasks))
    print("{}: {} completed tasks".format(employee_name, num_completed_tasks))
    print("Total tasks: {}".format(total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))

# Test the function
employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)


if __name__ == '__main__':
    employee_id = int(input('Enter the employee ID: '))
    get_employee_todo_progress(employee_id)
