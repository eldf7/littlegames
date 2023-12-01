from fun_rps_game import game_init
from guessing_number_game import guess_init
import sys

games = [
    "Rock, Paper, Scissors",
    "Rock, Paper, Scissors, Lizard, Spock",
    "Guess My Number"
]

ascii_art = """
 ∧＿∧
(｡･ω･｡)つ ━ ☆・*。 　
⊂　　 /　　 ・゜+. 　
しーＪ　　　°。+ *´¨)
 　　　　      .· ´*
                """

__indexed_choice__ = 0


def arcade_menu(name):
    global __indexed_choice__
    while True:
        print(f"{name}, please pick your game:")
        # Iterate through the games to display the choices.
        for index, game in enumerate(games, start=1):
            print(f"{index}. {game}")

        print(f"press x to quit")
        # Player makes a choice, stripped spaces, and converge to lowercase.
        choice = input().strip().lower()
        try:
            if choice in ["x", "quit"]:
                print(f"👋 Byeeee, {name}!\n" * 4)
                sys.exit(f"{ascii_art}")

            # Convert player choice to indexed choice for array use.
            elif (int(choice) - 1) in range(len(games)):
                __indexed_choice__ = int(choice) - 1
                break
        except ValueError:
            print("")
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
    print("🕹 WELCOME TO THE ARCADE!")
    while True:
        player_name = input(f"What's your name?\n").strip().title()
        if player_name:
            print("")
            arcade_menu(player_name)

