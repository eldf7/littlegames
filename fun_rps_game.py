import random
import sys


def game_init():
    __player_win__ = 0
    __computer_win__ = 0
    __tie__ = 0
    __total__ = 0

    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors",
        "4": "Lizard",
        "5": "Spock"
    }

    def __action_describes__(choice1, choice2):
        actions = {
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
        action = actions[(choice1, choice2)]
        return action

    def play_game(limit):
        nonlocal __player_win__
        nonlocal __computer_win__
        nonlocal __tie__
        nonlocal __total__

        while True:
            print(f"\n{player_name}, please select: ")
            for key, value in choices.items():
                if int(key) <= limit:
                    print(f"({key}) {value}")

            player_choice = input().strip().capitalize()
            try:
                player_choice = next(key for key, value in choices.items() if
                                     value == player_choice or key == player_choice)
                # if int(player_choice) <= limit:
                break
            except StopIteration:
                continue

        while True:
            computer_choice = random.choice(list(choices.keys()))
            if int(computer_choice) <= limit:
                break

        print(f"\n{player_name} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")
        __total__ += 1

        if choices[player_choice] == choices[computer_choice]:
            print(f"😳 {player_name.upper()} AND COMPUTER TIE!")
            __tie__ += 1
        elif (choices[player_choice] == "Rock" and choices[computer_choice] in ["Scissors", "Lizard"]) \
                or (choices[player_choice] == "Paper" and choices[computer_choice] in ["Rock", "Spock"]) \
                or (choices[player_choice] == "Scissors" and choices[computer_choice] in ["Paper", "Lizard"]) \
                or (choices[player_choice] == "Lizard" and choices[computer_choice] in ["Paper", "Spock"]) \
                or (choices[player_choice] == "Spock" and choices[computer_choice] in ["Rock", "Scissors"]):
            print(
                f"-{choices[player_choice]} {__action_describes__(choices[player_choice], choices[computer_choice])} {choices[computer_choice]}.\n"
                f"🎉 {player_name.upper()} WINS!")
            __player_win__ += 1
        else:
            print(
                f"-{choices[computer_choice]} {__action_describes__(choices[computer_choice], choices[player_choice])} {choices[player_choice]}.\n"
                f"🤖 COMPUTER WINS!")
            __computer_win__ += 1

        print(f"{player_name}: {__player_win__} | Computer: {__computer_win__} | Tie: {__tie__}")
        print(f"{__total__} {'game' if __total__ in [1, -1] else 'games'} played")

        repeat_play = input("\n****play again?**** (press y or enter to continue): ").strip().lower()
        if repeat_play in ["y", "yes", ""]:
            play_game(limit)
        else:
            sys.exit(f"👋 Thanks for playing my game, {player_name}! Byeeee.\n" * 4)

    return play_game


fun_rps = game_init()

if __name__ == "__main__":
    player_name = input("👋 Welcome to my game! What's your name?\n").title()
    fun_rps(5)

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
