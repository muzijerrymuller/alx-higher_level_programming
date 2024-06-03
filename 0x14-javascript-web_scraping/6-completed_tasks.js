#!/usr/bin/node
import requests
def get_completed_tasks(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
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

    if not user_task_counts:
        print("No users with completed tasks found.")
    else:
        for user_id, count in user_task_counts.items():
            print(f"User ID {user_id} has completed {count} tasks")

if __name__ == "__main__":
    # Example URLs based on your test cases
    api_urls = [
        "http://localhost:5050/route_0",
        "http://localhost:5050/route_1",
        "http://localhost:5050/route_2",
        "http://localhost:5050/route_3",
        "http://localhost:5050/route_4"
    ]
    
    for url in api_urls:
        print(f"Fetching data from {url}")
        get_completed_tasks(url)
        print("-" * 50)
