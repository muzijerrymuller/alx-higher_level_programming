#!/usr/bin/env python3
import requests

def get_completed_tasks(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from API. Error: {e}")
        return

    tasks = response.json()

    user_task_counts = {}

    for task in tasks:
        if task['completed']:
            user_id = task['userId']
            if user_id in user_task_counts:
                user_task_counts[user_id] += 1
            else:
                user_task_counts[user_id] = 1

    for user_id, count in user_task_counts.items():
        print(f"User ID {user_id} has completed {count} tasks")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos"
    get_completed_tasks(api_url)
