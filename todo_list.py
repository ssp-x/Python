todo_list = []

while True:
    if not todo_list:
        print("\nYour ToDo list is empty")
    else:
        print("\nYour ToDo list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        new_task = input("Enter the task: ").strip()
        if new_task:
            todo_list.append(new_task)
            print(f"Added: '{new_task}'")
        else:
            print("No task entered; nothing added.")
    elif choice == "2":
        if not todo_list:
            print("Nothing to remove; the list is empty.")
            continue
        try:
            idx_str = input("Enter the number of the task to remove: ").strip()
            idx = int(idx_str)
            if 1 <= idx <= len(todo_list):
                removed = todo_list.pop(idx - 1)
                print(f"Removed: '{removed}'")
            else:
                print(f"Please enter a number between 1 and {len(todo_list)}.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        print("Quitting.")
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
