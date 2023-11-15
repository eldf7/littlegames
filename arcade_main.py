from fun_rps_game import game_init
from guessing_number_game import guess_init
import sys

games = [
    "Rock, Paper, Scissors",
    "Rock, Paper, Scissors, Lizard, Spock",
    "Guess My Number"
]

__indexed_choice__ = 0


def arcade_menu(name):
    global __indexed_choice__
    while True:
        print(f"{name}, please pick your game:")
        # Iterate through the games to display the choices.
        for index, game in enumerate(games, start=1):
            print(f"{index}. {game}")

        print(f"press x to quit")
        # Player makes an index choice.
        choice = input().strip().lower()
        try:
            if choice in ["x", "quit"]:
                sys.exit(f"👋 Byeeee, {name}!\n" * 4)

            elif (int(choice) - 1) in range(len(games)):
                __indexed_choice__ = int(choice) - 1
                break
        except ValueError:
            continue

    if __indexed_choice__ == 0:
        print(f"\n👋 Welcome to {games[__indexed_choice__]}!")
        rps = game_init()
        # Parameter 3 for classic RPS
        rps(name, 3)
    elif __indexed_choice__ == 1:
        print(f"\n👋 Welcome to {games[__indexed_choice__]}!")
        rpsls = game_init()
        # Parameter 5 for improved RPSLS
        rpsls(name, 5)
    elif __indexed_choice__ == 2:
        print(f"\n👋 Welcome to {games[__indexed_choice__]}!")
        guess_number = guess_init()
        guess_number(name)

    print("🕹 WELCOME BACK TO THE ARCADE!")
    arcade_menu(name)


if __name__ == "__main__":
    player_name = input(f"🕹 WELCOME TO THE ARCADE!\nWhat's your name?\n").title()
    print("")
    arcade_menu(player_name)
