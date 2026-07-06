contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("✅ Contact Added Successfully!")

    elif choice == 2:
        if len(contacts) == 0:
            print("📒 No contacts available.")
        else:
            print("\n----- Contacts -----")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == 3:
        search = input("Enter contact name: ")

        if search in contacts:
            print("📞 Phone Number:", contacts[search])
        else:
            print("❌ Contact not found!")

    elif choice == 4:
        delete = input("Enter contact name to delete: ")

        if delete in contacts:
            del contacts[delete]
            print("🗑️ Contact Deleted Successfully!")
        else:
            print("❌ Contact not found!")

    elif choice == 5:
        print("👋 Thank you for using Contact Book!")
        break

    else:
        print("❌ Invalid Choice!")
