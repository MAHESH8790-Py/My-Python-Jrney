tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task Added Successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("📋 No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("❌ No tasks to delete.")
        else:
            task = input("Enter task to delete: ")
            if task in tasks:
                tasks.remove(task)
                print("🗑️ Task Deleted Successfully!")
            else:
                print("⚠️ Task not found!")

    elif choice == 4:
        print("👋 Thank you for using To-Do List!")
        break

    else:
        print("❌ Invalid Choice! Please enter 1-4.")