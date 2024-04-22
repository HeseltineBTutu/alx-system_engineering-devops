#!/usr/bin/python3
"""
This script fetches and displays employee TODO list progress
using a provided REST API.
"""

import sys
import requests


def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and prints it.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee info
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        employee_name = employee_data.get("name", "Unknown")

        # Fetch todos for the employee
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Calculate progress
        total_tasks = len(todos)
        done_tasks = [todo for todo in todos if todo.get("completed")]
        num_done_tasks = len(done_tasks)

        # Print progress report
        progress_message = (
                f"Employee {employee_name} is done with tasks "
                f"({num_done_tasks}/{total_tasks}):"
                )
        print(progress_message)
        for task in done_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
