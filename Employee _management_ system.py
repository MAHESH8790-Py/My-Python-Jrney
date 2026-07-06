employees = []

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        employee = input("Enter employee name: ")
        employees.append(employee)
        print("Employee added successfully!")

    elif ch == "2":
        if employees:
            print("\nEmployee List:")
            for employee in employees:
                print("-", employee)
        else:
            print("No employees found!")

    elif ch == "3":
        employee = input("Enter employee name: ")

        if employee in employees:
            print("Employee found!")
        else:
            print("Employee not found!")

    elif ch == "4":
        print("Thanks for using Employee Management System!")
        break

    else:
        print("Invalid choice!")
