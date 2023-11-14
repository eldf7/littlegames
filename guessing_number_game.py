import random
import sys


# Function to initialize and set up the game environment.
def guess_init():
    # Main game loop function
    def play_guess_number(name):
        # Computer makes a random choice within 1 to 5
        computer_choice = random.randint(1, 10)

        print(f"{name}, guess which number I'm thinking...")
        while True:
            guess = input()
            try:
                if int(guess) == computer_choice:
                    break
                else:
                    print("Hmmm...not quite. Try again.")
            except ValueError:
                print("Hmmm...not quite. Try again.")
                continue

        print(f"😳You guessed it! I was thinking {computer_choice}!")

        repeat_play = input(
            "\nThanks for playing with me. Want to guess again? (press y or enter to continue): ").strip().lower()
        # Check if the player wants to play again by examining the entered input.
        # If the input is 'y', 'yes', or an empty string (Enter key pressed), proceed with another round.
        if repeat_play in ["y", "yes", ""]:
            # initiate another round by recursively calling the play_guess_number function with the specified preference.
            play_guess_number(name)
        else:
            print("")

    # Return the play_guess_number function, creating a closure.
    return play_guess_number
