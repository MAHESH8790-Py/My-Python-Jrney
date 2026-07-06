students = {}

while True:
    print("\n===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Grade")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        try:
            name = input("Enter student name: ")
            marks = int(input("Enter student marks: "))

            students[name] = marks
            print("Student added successfully!")

        except ValueError:
            print("Please enter valid marks!")

    elif ch == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            print("\nStudent List:")
            for name, marks in students.items():
                print(name, "-", marks)

    elif ch == "3":
        name = input("Enter student name to search: ")

        if name in students:
            print("Student Found!")
            print("Marks:", students[name])
        else:
            print("Student not found!")

    elif ch == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif ch == "5":
        name = input("Enter student name: ")

        if name in students:
            marks = students[name]

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "Fail"

            print("Student:", name)
            print("Marks:", marks)
            print("Grade:", grade)

        else:
            print("Student not found!")

    elif ch == "6":
        print("🎉 Thanks for using Student Grade Management System!")
        break

    else:
        print("Invalid choice!")