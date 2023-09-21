# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to mark a task as complete
def mark_complete(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] += " [Done]"
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as complete: "))
        mark_complete(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task number to delete: "))
        delete_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
