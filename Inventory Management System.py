items = []

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        item = input("Enter item name: ")
        items.append(item)
        print("Item added successfully!")

    elif ch == "2":
        if items:
            print("\nItem List:")
            for item in items:
                print("-", item)
        else:
            print("No items found!")

    elif ch == "3":
        item = input("Enter item name to search: ")

        if item in items:
            print("Item found!")
        else:
            print("Item not found!")

    elif ch == "4":
        print("Thanks for using Inventory Management System!")
        break

    else:
        print("Invalid choice!")