import random
import sys


# Function to initialize and set up the game environment.
def guess_init():
    __total__ = 0

    # Main game loop function
    def play_guess_number(name):
        nonlocal __total__
        __guess_count__ = 0
        # Computer makes a random choice within randomly generated max,
        # and randomly generated min that's at least one less than generated max.
        maxguess = random.randint(2, 10)
        minguess = random.randint(1, maxguess - 1)
        computer_choice = random.randint(minguess, maxguess)

        print(f"{name}, guess which number I'm thinking of...")
        if (maxguess - minguess) == 1:
            print(f"(hint: it's either {minguess} or {maxguess}...🤫)")
        else:
            print(f"(hint: it's between {minguess} and {maxguess}, {minguess} and {maxguess} included...🤫)")
        while True:
            guess = input()
            __guess_count__ += 1
            try:
                if guess == "quit":
                    print("Thanks for playing!\n")
                    return
                elif int(guess) != computer_choice:
                    print("Hmmm...not quite. Guess again.")
                else:
                    if __guess_count__ / ((maxguess - minguess) + 1) < 0.5:
                        print(f"😳You guessed it! I was thinking of {computer_choice}!")
                    else:
                        print(f"😄You guessed it! I was thinking of {computer_choice}!")
                    __total__ += 1
                    break
            except ValueError:
                print("Please enter a valid number or type 'quit' to quit.")
                continue

        repeat_play = input(
            f"\nThanks for playing with me. Want to guess another? \n"
            f"({__total__} {'number' if __total__ in [1, -1] else 'numbers'} guessed, press y or enter to play again): ").strip().lower()
        # Check if the player wants to play again by examining the entered input.
        # If the input is 'y', 'yes', or an empty string (Enter key pressed), proceed with another round.
        if repeat_play in ["y", "yes", ""]:
            # initiate another round by recursively calling the play_guess_number function with name.
            print("")
            play_guess_number(name)
        else:
            if __name__ == "__main__":
                sys.exit(f"👋 Thanks for playing my game, {player_name}! Byeeeee.\n" * 4)
            print("")
            return

    # Return the play_guess_number function, creating a closure.
    return play_guess_number


if __name__ == "__main__":
    # Initialize the game
    guessing_game = guess_init()

    # Get and validate player's name
    while True:
        player_name = input("👋 Welcome to my game! What's your name?\n").strip().title()
        if player_name:
            print("")
            break

    guessing_game(player_name)
