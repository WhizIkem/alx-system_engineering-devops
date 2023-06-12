#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the CSV format.
"""
import requests
import csv
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

    # Create CSV file
    filename = ("{}.csv".format(employee_id))
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])

        # Write tasks to CSV
        for task in todo_data:
            task_completed_status = "True" if task["completed"] else "False"
            writer.writerow([employee_id, employee_name, task_completed_status,
                            task["title"]])

    print("Data exported to {} successfully.".format(filename))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
