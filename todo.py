# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_number - 1)
            print(f"Removed task: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
