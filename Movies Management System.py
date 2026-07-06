movies = []

while True:
    print("\n===== Movie Collection Management System =====")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        movie = input("Enter movie name: ")
        movies.append(movie)
        print("Movie added successfully! 🎬")

    elif ch == "2":
        if movies:
            print("\nMovie List:")
            for movie in movies:
                print("-", movie)
        else:
            print("No movies found!")

    elif ch == "3":
        movie = input("Enter movie name to search: ")

        if movie in movies:
            print("Movie found! 🎬")
        else:
            print("Movie not found!")

    elif ch == "4":
        print("Thanks for using Movie Collection Management System! 🎬")
        break

    else:
        print("Invalid choice!")