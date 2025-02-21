import json
from datetime import datetime

class Task:
    """
    Represents a single task with attributes such as name, description,
    due date, priority level, and status.
    """
    def __init__(self, name, description, due_date, priority, status="Pending"):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        """Converts the task object into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

class TaskManager:
    """
    Manages a collection of tasks: adding, viewing, updating, and deleting tasks.
    """
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully! ✅")

    def view_tasks(self, sort_by=None):
        """Displays all tasks, sorted by deadline or priority if specified."""
        if not self.tasks:
            print("No tasks available. Start by adding a new task! 📝")
            return
        
        if sort_by == "priority":
            self.tasks.sort(key=lambda t: t.priority)
        elif sort_by == "due_date":
            self.tasks.sort(key=lambda t: datetime.strptime(t.due_date, "%Y-%m-%d"))
        
        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.name} - {task.description} | Due: {task.due_date} | Priority: {task.priority} | Status: {task.status}")

    def update_task(self, task_name, new_status=None, new_due_date=None, new_priority=None):
        """Updates an existing task's details."""
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                if new_status:
                    task.status = new_status
                if new_due_date:
                    task.due_date = new_due_date
                if new_priority:
                    task.priority = new_priority
                self.save_tasks()
                print("Task updated successfully! ✏️")
                return
        print("Task not found. ❌")

    def delete_task(self, task_name):
        """Removes a task from the list."""
        self.tasks = [task for task in self.tasks if task.name.lower() != task_name.lower()]
        self.save_tasks()
        print("Task deleted successfully! ❌")

    def save_tasks(self):
        """Saves the task list to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        """Loads tasks from the JSON file on startup."""
        try:
            with open(self.filename, "r") as file:
                task_dicts = json.load(file)
                self.tasks = [Task(**task) for task in task_dicts]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

# Main execution
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\nTask Manager App 📝")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter task name: ")
            desc = input("Enter description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            manager.add_task(Task(name, desc, due, priority))
        
        elif choice == "2":
            sort_option = input("Sort by (priority/due_date/none): ")
            manager.view_tasks(sort_by=sort_option if sort_option in ["priority", "due_date"] else None)
        
        elif choice == "3":
            task_name = input("Enter task name to update: ")
            new_status = input("Enter new status (Pending/Done): ") or None
            new_due_date = input("Enter new due date (YYYY-MM-DD) or leave blank: ") or None
            new_priority = input("Enter new priority (High/Medium/Low) or leave blank: ") or None
            manager.update_task(task_name, new_status, new_due_date, new_priority)
        
        elif choice == "4":
            task_name = input("Enter task name to delete: ")
            manager.delete_task(task_name)
        
        elif choice == "5":
            print("Exiting Task Manager. Goodbye! 🚀")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")
