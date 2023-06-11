#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(base_url, employee_id)
    todos_url = '{}/todos?userId={}'.format(base_url, employee_id)

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        employee_response.raise_for_status()
        todos_response.raise_for_status()

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        employee_name = employee_data['name']

        completed_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos_data)

        print('Employee {} is done with tasks ({}/{}):'.format(employee_name,
              number_of_done_tasks, total_number_of_tasks))
        print('{}: {}/{}'.format(employee_name, number_of_done_tasks,
              total_number_of_tasks))

        for task in completed_tasks:
            print('\t{}'.format(task['title']))

    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))


if __name__ == '__main__':
    employee_id = int(input('Enter the employee ID: '))
    get_employee_todo_progress(employee_id)
