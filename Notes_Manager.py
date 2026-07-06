while True:
    print("\n===== Notes Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\n===== Your Notes =====")
                print(file.read())

        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Thanks for using Notes Manager!")
        break

    else:
        print("Invalid choice!")