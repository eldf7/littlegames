import random

name = input("Welcome to My Game! What's your name?\n").upper()
while True:
    choice = input(f"\n{name.capitalize()}, please select: \n (1) Rock\n (2) Paper\n (3) Scissor\n").lower()
    if choice in ["1", "2", "3", "rock", "paper", "scissor"]:
        break

player_choice = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissor",
    "rock": "Rock",
    "paper": "Paper",
    "scissor": "Scissor"
}

computer_choice = random.choice(["Rock", "Paper", "Scissor"])
print(f"You picked {player_choice[choice]}, Computer picked {computer_choice}")

if player_choice[choice] == computer_choice:
    print(f"~~~~~~~~~~{name} and Computer TIE!~~~~~~~~~~")
elif player_choice[choice] == "Rock" and computer_choice == "Scissor":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
elif player_choice[choice] == "Paper" and computer_choice == "Rock":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
elif player_choice[choice] == "Scissor" and computer_choice == "Paper":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
else:
    print("~~~~~~~~~~COMPUTER WINS!~~~~~~~~~~")
