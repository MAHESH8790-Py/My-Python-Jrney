import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))

        if guess < number:
            print("Too Low! Try Again.")

        elif guess > number:
            print("Too High! Try Again.")

        else:
            print("🎉 Congratulations! You guessed the number!")
            break

    except ValueError:
        print("Please enter a valid number!")
