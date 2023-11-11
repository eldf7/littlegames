import random
import sys


def print_keys_values(keys_values):
    for key, value in keys_values.items():
        print(f"({key}) {value} ")


choices = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}

name = input("👋 Welcome to my game! What's your name?\n").title()

while True:
    while True:
        print(f"\n{name}, please select: ")
        print_keys_values(choices)
        player_choice = input().strip().capitalize()
        try:
            player_choice = next(key for key, value in choices.items() if
                                 value == player_choice or key == player_choice)
            break
        except StopIteration:
            continue

    computer_choice = random.choice(list(choices.keys()))

    print(f"\n{name} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")

    if choices[player_choice] == choices[computer_choice]:
        print(f"😳 {name.upper()} AND COMPUTER TIE!")
    elif (choices[player_choice] == "Rock" and choices[computer_choice] == "Scissors") \
            or (choices[player_choice] == "Paper" and choices[computer_choice] == "Rock") \
            or (choices[player_choice] == "Scissors" and choices[computer_choice] == "Paper"):
        print(f"🎉 {name.upper()} WINS!")
    else:
        print("🤖 COMPUTER WINS!")

    repeat_play = input("****play again?**** (press y to continue): ").strip().lower()
    if repeat_play in ("y", "yes", ""):
        continue
    else:
        sys.exit("👋 Thanks for playing my game! Byeeee. \n")
