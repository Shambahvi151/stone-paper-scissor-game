import random

choices = ["stone", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter stone, paper, or scissors: ").lower()

print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice!")

elif user == computer:
    print("It's a tie!")

elif (user == "stone" and computer == "scissors") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissors" and computer == "paper"):
    print(" Maa win!")

else:
    print("Computer wins!")

