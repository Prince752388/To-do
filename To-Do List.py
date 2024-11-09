import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Function to display the list of tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added!")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to update: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            new_task = input("Enter the new description for the task: ")
            tasks[task_number - 1] = new_task
            print(f"Task {task_number} has been updated to '{new_task}'.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been deleted.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = []  # List to store tasks

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
