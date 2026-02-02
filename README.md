# To-Do List Application

A simple command-line to-do list application built with Python. This lightweight tool helps you manage your daily tasks directly from your terminal.

## Features

- ✅ **View Tasks** - Display all your current tasks in a numbered list
- ➕ **Add Tasks** - Quickly add new tasks to your list
- ❌ **Delete Tasks** - Remove completed or unwanted tasks
- 🎯 **Simple Interface** - Easy-to-use menu-driven interface

## How It Works

The application uses a simple Python list to store tasks in memory during runtime. It provides an interactive menu system where you can choose from four options:

### Main Functions

1. **`show_menu()`** - Displays the main menu with available options
2. **`view_tasks()`** - Shows all current tasks with their numbers
3. **`add_task()`** - Prompts user to enter a new task and adds it to the list
4. **`delete_task()`** - Allows user to remove a task by its number

## Installation

1. Clone this repository:
```bash
git clone https://github.com/thatjelvin/To-do.git
cd To-do
```

2. Make sure you have Python installed (Python 3.x recommended)

## Usage

Run the application from your terminal:

```bash
python todo.py
```

You'll see a menu like this:

```
--- TO-DO LIST ---
1. View tasks
2. Add a task
3. Delete a task
4. Exit
Choose an option (1-4):
```

### Examples

**Adding a task:**
- Select option `2`
- Type your task (e.g., "Buy groceries")
- Press Enter

**Viewing tasks:**
- Select option `1`
- All tasks will be displayed with numbers

**Deleting a task:**
- Select option `3`
- Enter the number of the task you want to delete

**Exiting:**
- Select option `4` to close the application

## Code Structure

- **Global Variable**: `tasks = []` - Stores all tasks in a list
- **Main Loop**: Continuously displays menu and processes user input
- **Error Handling**: Validates user input for task deletion to prevent crashes

## Limitations

- Tasks are stored in memory only and will be lost when the program exits
- No data persistence (tasks are not saved to a file)
- Basic text-only interface

## Future Improvements

Potential enhancements could include:
- Save tasks to a file for persistence
- Mark tasks as complete without deleting them
- Add task priorities or categories
- Set due dates for tasks
- Search functionality

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [@thatjelvin](https://github.com/thatjelvin)