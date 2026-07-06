patients = []

while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        patient = input("Enter patient name: ")
        patients.append(patient)
        print("Patient added successfully!")

    elif ch == "2":
        if patients:
            print("\nPatient List:")
            for patient in patients:
                print("-", patient)
        else:
            print("No patients found!")

    elif ch == "3":
        patient = input("Enter patient name to search: ")

        if patient in patients:
            print("Patient found!")
        else:
            print("Patient not found!")

    elif ch == "4":
        print("Thanks for using Hospital Management System!")
        break

    else:
        print("Invalid choice!")
