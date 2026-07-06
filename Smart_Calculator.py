while True:
    print("\n===== Smart Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = a + b
            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

    elif ch == "2":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = a - b
            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

    elif ch == "3":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = a * b
            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

    elif ch == "4":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = a / b
            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

        except ZeroDivisionError:
            print("Cannot divide by zero!")

    elif ch == "5":
        print("Thanks for using Smart Calculator!")
        break

    else:
        print("Invalid choice!")