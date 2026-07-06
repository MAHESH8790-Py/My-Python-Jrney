books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if books:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)
        else:
            print("No books found.")

    elif choice == "3":
        book = input("Enter book name to search: ")

        if book in books:
            print("Book found.")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Program finished.")
        break

    else:
        print("Invalid choice.")