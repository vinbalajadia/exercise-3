# List to store all tasks
tasks = []


def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print("Task added!")


def show_tasks():
    """Display all tasks with numbering."""
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(task_number):
    """Remove a task by its number if it exists."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)  # list index starts at 0
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number.")


def main():
    """Main menu loop for the To-Do app."""
    while True:
        # Display menu options
        print("\n=== To-Do App ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            # Add a new task
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            # Show all tasks
            show_tasks()

        elif choice == "3":
            # Remove a task by number
            try:
                task_no = int(input("Enter task number to remove: "))
                remove_task(task_no)
            except ValueError:
                # Handle non-integer input
                print("Please enter a valid number.")

        elif choice == "4":
            # Exit the app
            print("Exiting... Goodbye!")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice! Please try again.")


# Run the program only if executed directly
if __name__ == "__main__":
    main()