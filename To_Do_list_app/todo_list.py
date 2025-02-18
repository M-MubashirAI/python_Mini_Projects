# 2️⃣ To-Do List (Lists & File Handling) ✅
# 🔹 Description: Develop a CLI-based To-Do List where users can:
# ✅ Add a task
# ✅ Mark a task as completed
# ✅ View all tasks
# ✅ Save tasks in a file (so they don’t disappear after the program exits)

# 🔹 Concepts Used: Lists, file handling, loops, functions
# todo_list.py
# A CLI-based To-Do List with persistent file storage

import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file or return empty list if file doesn't exist"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"description": task, "completed": False})
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    """Display all tasks with completion status"""
    if not tasks:
        print("No tasks in the list!")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['description']}")

def complete_task(tasks):
    """Mark a task as completed"""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print(f"Marked task as complete: {tasks[task_num]['description']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    main()