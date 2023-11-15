from fun_rps_game import game_init
from guessing_number_game import guess_init
import sys

games = [
    "Rock, Paper, Scissors",
    "Rock, Paper, Scissors, Lizard, Spock",
    "Guess My Number"
]

name = input(f"WELCOME TO THE ARCADE!\nWhat's your name?\n").title()
print("")


def arcade_menu():
    global name
    while True:
        print(f"{name}, please pick your game:")
        # Iterate through the games to display the choices.
        for index, game in enumerate(games, start=1):
            print(f"{index}. {game}")

        print(f"press x to quit")
        # Player makes a choice.
        # The input is stripped of leading/trailing whitespaces and capitalized to ensure correct mapping.
        choice = input().strip().lower()
        try:
            if choice in ["x", "quit"]:
                sys.exit(f"👋 Byeeee, {name}!\n" * 4)
            elif (int(choice) - 1) in range(len(games)):
                break
        except ValueError:
            continue

    if int(choice) == 1:
        print(f"\n👋 Welcome to {games[0]}!")
        rps = game_init()
        rps(name, 3)
    elif int(choice) == 2:
        print(f"\n👋 Welcome to {games[1]}!")
        rpsls = game_init()
        rpsls(name, 5)
    else:
        print(f"\n👋 Welcome to {games[2]}!")
        guess_number = guess_init()
        guess_number(name)

    # Prompt the player to decide whether to play another round.
    # The input statement waits for the user to provide input, which is then stripped of leading/trailing whitespaces
    # and converted to lowercase for case-insensitive comparison.
    print("WELCOME BACK TO THE ARCADE!")
    arcade_menu()


if __name__ == "__main__":
    arcade_menu()
