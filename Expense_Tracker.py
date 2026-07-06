expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        try:
            amount = float(input("Enter expense amount: "))
            expenses.append(amount)
            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount!")

    elif ch == "2":
        if len(expenses) == 0:
            print("No expenses found!")
        else:
            print("\nExpenses:")
            for expense in expenses:
                print("₹", expense)

    elif ch == "3":
        print("Total Expense: ₹", sum(expenses))

    elif ch == "4":
        print("Thanks for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")