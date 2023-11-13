import random
import sys


def game():
    player_win = 0
    computer_win = 0
    tie = 0
    total = 0

    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors",
        "4": "Lizard",
        "5": "Spock"
    }

    def describes(choice1, choice2):
        descriptors = {
            ("Rock", "Scissors"): "crushes",
            ("Rock", "Lizard"): "crushes",
            ("Paper", "Rock"): "covers",
            ("Paper", "Spock"): "disapproves",
            ("Scissors", "Paper"): "cuts",
            ("Scissors", "Lizard"): "decapitates",
            ("Lizard", "Paper"): "eats",
            ("Lizard", "Spock"): "poisons",
            ("Spock", "Rock"): "vaporizes",
            ("Spock", "Scissors"): "smashes"
        }
        descriptor = descriptors[(choice1, choice2)]
        return descriptor

    def play_game(limit):
        nonlocal player_win
        nonlocal computer_win
        nonlocal tie
        nonlocal total

        while True:
            print(f"\n{name}, please select: ")
            for key, value in choices.items():
                if int(key) <= limit:
                    print(f"({key}) {value}")

            player_choice = input().strip().capitalize()
            try:
                player_choice = next(key for key, value in choices.items() if
                                     value == player_choice or key == player_choice)
                # if int(player_choice) <= limit:
                #     break
            except StopIteration:
                continue

        while True:
            computer_choice = random.choice(list(choices.keys()))
            if int(computer_choice) <= limit:
                break

        print(f"\n{name} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")
        total += 1

        if choices[player_choice] == choices[computer_choice]:
            print(f"😳 {name.upper()} AND COMPUTER TIE!")
            tie += 1
        elif (choices[player_choice] == "Rock" and choices[computer_choice] in ["Scissors", "Lizard"]) \
                or (choices[player_choice] == "Paper" and choices[computer_choice] in ["Rock", "Spock"]) \
                or (choices[player_choice] == "Scissors" and choices[computer_choice] in ["Paper", "Lizard"]) \
                or (choices[player_choice] == "Lizard" and choices[computer_choice] in ["Paper", "Spock"]) \
                or (choices[player_choice] == "Spock" and choices[computer_choice] in ["Rock", "Scissors"]):
            print(f"-{choices[player_choice]} {describes(choices[player_choice], choices[computer_choice])} {choices[computer_choice]}.\n"
                  f"🎉 {name.upper()} WINS!")
            player_win += 1
        else:
            print(f"-{choices[computer_choice]} {describes(choices[computer_choice], choices[player_choice])} {choices[player_choice]}.\n"
                  f"🤖 COMPUTER WINS!")
            computer_win += 1

        print(f"{name}: {player_win} | Computer: {computer_win} | Tie: {tie}")
        print(f"{total} {'game' if total in [1, -1] else 'games'} played")

        repeat_play = input("\n****play again?**** (press y or enter to continue): ").strip().lower()
        if repeat_play in ["y", "yes", ""]:
            play_game(limit)

    return play_game


name = input("👋 Welcome to my game! What's your name?\n").title()
a_game = game()
a_game(3)
sys.exit(f"👋 Thanks for playing my game, {name}! Byeeee.\n")

# Rock > Scissors
# Spock > Rock
# Paper > Spock
# Lizard > Paper
# Scissors > Lizard

# Spock > Scissors
# Lizard > Spock
# Rock > Lizard
# Paper > Rock
# Scissors > Paper

# Scissors > Paper > Rock > Lizard > Spock > Scissor > Lizard > Paper > Spock > Rock > Scissors

# Rock > Scissors
# Paper > Rock
# Scissors > Paper
# Scissors > Paper > Rock > Scissors
