import random

game = ["rock", "paper", "scissors"]

computer = random.choice(game)

user = input("Enter Rock, Paper or Scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("🤝 It's a Tie!")

elif user == "rock" and computer == "scissors":
    print("🎉 You Win!")

elif user == "paper" and computer == "rock":
    print("🎉 You Win!")

elif user == "scissors" and computer == "paper":
    print("🎉 You Win!")

else:
    print("🤖 Computer Wins!")