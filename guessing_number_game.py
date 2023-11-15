import random
import sys

# Function to initialize and set up the game environment.
def guess_init():
    # Main game loop function
    def play_guess_number(name):
        # Computer makes a random choice within 1 to 5
        minguess = 1
        maxguess = random.randint(5, 10)
        computer_choice = random.randint(minguess, maxguess)

        print(f"{name}, guess which number I'm thinking of...\n"
              f"(hint: it's between {minguess} and {maxguess}...🤫)")
        while True:
            guess = input()
            try:
                if guess == "quit":
                    print("Thanks for playing!\n")
                    return
                elif int(guess) != computer_choice:
                    print("Hmmm...not quite. Try again.")
                else:
                    print(f"😳You guessed it! I was thinking of {computer_choice}!")
                    break
            except ValueError:
                print("Hmmm...not quite. Try again.")
                continue

        repeat_play = input(
            "\nThanks for playing with me. Want to guess again? (press y or enter to continue): ").strip().lower()
        # Check if the player wants to play again by examining the entered input.
        # If the input is 'y', 'yes', or an empty string (Enter key pressed), proceed with another round.
        if repeat_play in ["y", "yes", ""]:
            # initiate another round by recursively calling the play_guess_number function with the specified preference.
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

    # Get player's name
    player_name = input("👋 Welcome to my game! What's your name?\n").title()
    print("")

    # Start the game with predefined preference.
    # 3 for classic Rock-Paper-Scissors,
    # 5 for improved to Rock-Paper-Scissors-Lizard-Spock
    guessing_game(player_name)
