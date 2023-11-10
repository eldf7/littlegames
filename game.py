import random


def print_keys_values(keys_values):
    for key, value in keys_values.items():
        print(f"({key}) {value} ")


choices = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}

name = input("Welcome to My Game! What's your name?\n").upper()

while True:
    print(f"\n{name.capitalize()}, please select: ")
    print_keys_values(choices)
    player_choice = input().capitalize()
    if player_choice in choices:
        break
    if player_choice in choices.values():
        player_choice = next(key for key, value in choices.items() if value == player_choice)
        break

computer_choice = random.choice(list(choices.keys()))

print(f"{name.capitalize()} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")

if choices[player_choice] == choices[computer_choice]:
    print(f"~~~~~~~~~~{name} and Computer TIE!~~~~~~~~~~")
elif choices[player_choice] == "Rock" and choices[computer_choice] == "Scissors":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
elif choices[player_choice] == "Paper" and choices[computer_choice] == "Rock":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
elif choices[player_choice] == "Scissors" and choices[computer_choice] == "Paper":
    print(f"~~~~~~~~~~{name} WINS!~~~~~~~~~~")
else:
    print("~~~~~~~~~~COMPUTER WINS!~~~~~~~~~~")
