#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    employee_url = '{}/users/{}'.format(base_url, employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Retrieve employee's TODO list
    todos_url = '{}/todos?userId={}'.format(base_url, employee_id)
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate TODO list progress
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Print employee TODO list progress
    print('Employee {} is done with tasks ({}/{}):'.format(employee_name,
          number_of_done_tasks, total_number_of_tasks))
    print('{}: {}/{}'.format(employee_name, number_of_done_tasks,
                             total_number_of_tasks))

    for task in completed_tasks:
        print('\t{}'.format(task['title']))


if __name__ == '__main__':
    employee_id = int(input('Enter the employee ID: '))
    get_employee_todo_progress(employee_id)
