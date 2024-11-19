# Task manager

import json

def save_tasks(tasks):
    with open("a15_tasks.json", "w") as file:
        json.dump(tasks, file)
        print("Tasks saved.")

def load_tasks():
    try:
        with open("a15_tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No file found.")
        return []

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("What is priority of task (high, medium, low)? ").lower()
    tasks.append({"task": task_name, "priority": priority, "done": False})
    save_tasks(tasks)

def list_tasks(tasks):
    priorities = {"high": 1, "medium": 2, "low": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priorities.get(x["priority"], 4))
    print("\n--Tasks!--")
    for task in sorted_tasks:
        status = "Done" if task["done"] else "Pending"
        print(f"{task['task']} ({task['priority']}) - {status}")
    print("-------------")

# Mark a task as done
def mark_task_done(tasks):
    task_name = input("Enter the task name to mark as done: ")
    for task in tasks:
        if task["task"].lower() == task_name.lower() and not task["done"]:
            task["done"] = True
            print(f"Marked '{task_name}' as done.")
            save_tasks(tasks)
            return
    print(f"Task '{task_name}' not found or already done.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                list_tasks(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                print("Exiting Task Manager. Goodbye!")
                save_tasks(tasks)
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main()