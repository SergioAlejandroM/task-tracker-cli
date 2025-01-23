import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

def add_task(description):
    if not description:
        print("Please provide a description for the task")
        return
    
    description = "".join(description)

    with open(FILE_NAME, "r+") as file:
        tasks = json.load(file)
        new_task = {
            "id": len(tasks) + 1,
            "description": description,
            "status": "ToDo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        tasks.append(new_task)
        file.seek(0)
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully (ID: {new_task['id']})")

def list_tasks(filter_status= None):
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
    
    if not tasks:
        print("No tasks found")
    
    if filter_status:
        tasks = [task for task in tasks if task["status"] ==  filter_status[0]]
    
    for task in tasks:
        print(f"[{task['status'].upper()}] ID: {task['id']} - {task['description']}")

def update_task(args):
    if len(args) < 2:
        print("Usage: task-cli update <id> <new-description>")
        return

    task_id = int(args[0])
    new_description = " ".join(args[1:])

    with open(FILE_NAME, "r+") as file:
        tasks = json.load(file)
        task = next((t for t in tasks if t["id"] == task_id), None)

        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        task["description"] = new_description
        task["updatedAt"] = datetime.now().isoformat()
        file.seek(0)
        json.dump(tasks, file, indent=4)

    print(f"Task ID {task_id} updated successfully.")

def delete_task(args):
    if not args:
        print("Usage: task-cli delete <id>")
        return

    task_id = int(args[0])

    with open(FILE_NAME, "r+") as file:
        tasks = json.load(file)
        tasks = [t for t in tasks if t["id"] != task_id]
        file.seek(0)
        json.dump(tasks, file, indent=4)
        file.truncate()

    print(f"Task ID {task_id} deleted successfully.")

def mark_task(args, status):
    if not args:
        print(f"Usage: task-cli mark-{status} <id>")
        return

    task_id = int(args[0])

    with open(FILE_NAME, "r+") as file:
        tasks = json.load(file)
        task = next((t for t in tasks if t["id"] == task_id), None)

        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        task["status"] = status
        task["updatedAt"] = datetime.now().isoformat()
        file.seek(0)
        json.dump(tasks, file, indent=4)

    print(f"Task ID {task_id} marked as {status}.")


def main():
    initialize_file()

    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: task-cli <Command> [options]")
        return

    command = args[0].lower()

    if command == "add":
        add_task(args[1:])
    elif command == "list":
        list_tasks(args[1:])
    elif command == "update":
        update_task(args[1:])
    elif command == "delete":
        delete_task(args[1:])
    elif command == "mark-in-progress":
        mark_task(args[1:], "in-progress")
    elif command == "mark-done":
        mark_task(args[1:], "done")
    else:
        print(f"Unkwon command: {command}")

if __name__ == "__main__":
    main()

