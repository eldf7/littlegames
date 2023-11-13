import random
import sys
choices = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}


def play_game():
    global tie
    global player_win
    global computer_win
    global total

    while True:
        print(f"\n{name}, please select: ")
        for key, value in choices.items():
            print(f"({key}) {value}")

        player_choice = input().strip().capitalize()
        try:
            player_choice = next(key for key, value in choices.items() if
                                 value == player_choice or key == player_choice)
            break
        except StopIteration:
            continue

    computer_choice = random.choice(list(choices.keys()))

    print(f"\n{name} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")
    total += 1

    if choices[player_choice] == choices[computer_choice]:
        print(f"😳 {name.upper()} AND COMPUTER TIE!")
        tie += 1
    elif (choices[player_choice] == "Rock" and choices[computer_choice] == "Scissors") \
            or (choices[player_choice] == "Paper" and choices[computer_choice] == "Rock") \
            or (choices[player_choice] == "Scissors" and choices[computer_choice] == "Paper"):
        print(f"🎉 {name.upper()} WINS!")
        player_win += 1
    else:
        print("🤖 COMPUTER WINS!")
        computer_win += 1

    print(f"{name}: {player_win} | Computer: {computer_win} | Tie: {tie}")
    print(f"{total} {'game' if total <= 1 else 'games'} played")

    repeat_play = input("\n****play again?**** (press y to continue): ").strip().lower()
    if repeat_play in ["y", "yes", ""]:
        play_game()


name = input("👋 Welcome to my game! What's your name?\n").title()
player_win = 0
computer_win = 0
tie = 0
total = 0
play_game()
sys.exit(f"👋 Thanks for playing my game, {name}! Byeeee.\n")

# Rock > Scissors
# Paper > Rock
# Scissors > Paper
# Scissors > Paper > Rock > Scissors

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

# Scissors > Paper > Rock > Lizard > Spock > Scissor (> Lizard > Paper > Spock > Rock > Scissors)
