tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added!")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\n=== To-Do App ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            try:
                task_no = int(input("Enter task number to remove: "))
                remove_task(task_no)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
