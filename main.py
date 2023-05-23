import datetime
from rich.console import Console

'''
    Aqentjus 2023
    https://github.com/Aqentjus
'''


console = Console()

def print_tasks(tasks):
    """Print all tasks in the given list."""
    if not tasks:
        console.print("No tasks in the list.")
    else:
        console.print("Tasks::")
        for i, task in enumerate(tasks):
            console.print(f"[blue]{i+1}. {task[0]}[/blue] ({task[1]})")

def add_task(tasks):
    """Add a new task to the given list."""
    task = input("Enter a new task: ")
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    tasks.append((task, timestamp))
    console.print(f"Task: '{task}' was sved to the list")

def remove_task(tasks):
    """Remove a task from the given list."""
    print_tasks(tasks)
    if tasks:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            task, timestamp = tasks.pop(index-1)
            console.print(f"Task: '{task}' was removed from the list")
        else:
            console.print("Invalid task number.")
    else:
        console.print("No tasks in the list.")

def write_tasks_to_file(tasks, filename):
    """Write tasks to a file."""
    with open(filename, "w") as f:
        for task, timestamp in tasks:
            f.write(f"{task} ({timestamp})\n")
    console.print(f"Tasks saved to the file: {filename}.")

def main():
    filename = "tasks.txt"
    try:
        with open(filename) as f:
            tasks = [line.strip().split(" (") for line in f]
            tasks = [(task, timestamp[:-1]) for task, timestamp in tasks]
    except FileNotFoundError:
        tasks = []

    while True:
        console.print("\nOptions:")
        console.print("1. Print all tasks")
        console.print("2. Add a new task")
        console.print("3. Remove a task")
        console.print("4. Quit the program")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            write_tasks_to_file(tasks, filename)
        elif choice == "3":
            remove_task(tasks)
            write_tasks_to_file(tasks, filename)
        elif choice == "4":
            write_tasks_to_file(tasks, filename)
            console.print("Program closed.")
            break
        else:
            console.print("Invalid choice.")


if __name__ == "__main__":
    main()