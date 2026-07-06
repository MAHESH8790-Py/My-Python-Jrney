balance = 1000

while True:
    print("\n===== ATM Management System =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        deposit_money = int(input("Enter money to deposit: "))
        balance += deposit_money
        print("Money deposited successfully!")

    elif choice == "3":
        withdraw_money = int(input("Enter money to withdraw: "))

        if withdraw_money <= balance:
            balance -= withdraw_money
            print("Money withdrawn successfully!")
        else:
            print("Insufficient funds!")

    elif choice == "4":
        print("Program finished!")
        break

    else:
        print("Invalid choice!")