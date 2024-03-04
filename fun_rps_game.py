import random
import sys


# Function to initialize and set up the game environment.
def game_init():
    # Initialize variables to keep track of game statistics.
    __player_win__ = 0
    __computer_win__ = 0
    __tie__ = 0
    __total__ = 0

    # Define choices for the game (mapping keys to corresponding game options).
    # When limit is 3, it's the classic RPS. Limit of 5 for expanded version played in The Big Bang Theory
    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors",
        "4": "Lizard",
        "5": "Spock"
    }

    # Define action description for each combination of choices.
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

    # Main game loop function
    def play_game(player_name, preference):
        # Declare variables as nonlocal to indicate that they refer to variables in the outer (enclosing) scope.
        # These variables are used to keep track of game statistics and are updated within the play_game function.
        nonlocal __player_win__
        nonlocal __computer_win__
        nonlocal __tie__
        nonlocal __total__

        while True:
            # Display the available choices to the player.
            print(f"{player_name}, please select: ")

            # Iterate through the choices dictionary to show the options.
            # Only display choices up to the specified preference.
            for key, value in choices.items():
                if int(key) <= preference:
                    print(f"({key}) {value}")

            # Player makes a choice.
            # The input is stripped of leading/trailing whitespaces and capitalized to ensure correct mapping.
            player_choice = input().strip().capitalize()
            try:

                # Use a generator expression to find the key corresponding to the player's choice.
                # The next() function is used to get the first matching key-value pair.
                # It checks both the key and value to handle cases where the user enters either the key or the value.
                player_choice = next(key for key, value in choices.items() if
                                     value == player_choice or key == player_choice)
                # Commented preference out for player_choice for a little fun and a way to hack
                # if int(player_choice) <= preference:
                break
            except StopIteration:
                print("")
                continue

        # Computer makes a random choice within preference
        while True:
            computer_choice = random.choice(list(choices.keys()))
            if int(computer_choice) <= preference:
                break

        # Display choices
        print(f"\n{player_name} picked {choices[player_choice]}, Computer picked {choices[computer_choice]}")
        # Increment the total number of games played with each time a new game is looped.
        __total__ += 1

        # Determine and display game outcomes. Update game statistics.
        if choices[player_choice] == choices[computer_choice]:
            print(f"😳 {player_name.upper()} AND COMPUTER TIE!")
            __tie__ += 1
        elif (choices[player_choice] == "Rock" and choices[computer_choice] in ["Scissors", "Lizard"]) \
                or (choices[player_choice] == "Paper" and choices[computer_choice] in ["Rock", "Spock"]) \
                or (choices[player_choice] == "Scissors" and choices[computer_choice] in ["Paper", "Lizard"]) \
                or (choices[player_choice] == "Lizard" and choices[computer_choice] in ["Paper", "Spock"]) \
                or (choices[player_choice] == "Spock" and choices[computer_choice] in ["Rock", "Scissors"]):
            print(
                # First part displays outcome explanation, i.e. Rock crushes Scissors, Scissors cuts paper and so on.
                f"-{choices[player_choice]} {__action_describes__(choices[player_choice], choices[computer_choice])} {choices[computer_choice]}.\n"
                f"🎉 {player_name.upper()} WINS!")
            __player_win__ += 1
        else:
            print(
                # Same as above, just for when computer wins
                f"-{choices[computer_choice]} {__action_describes__(choices[computer_choice], choices[player_choice])} {choices[player_choice]}.\n"
                f"🤖 COMPUTER WINS!")
            __computer_win__ += 1

        # Display overall statistics
        print(f"{player_name}: {__player_win__} | Computer: {__computer_win__} | Tie: {__tie__}")
        # This line uses a conditional expression to choose between 'game' and 'games' for proper grammar.
        # Adapting the wording based on whether it's singular or plural.
        print(f"{__total__} {'game' if __total__ in [1, -1] else 'games'} played")

        # Prompt the player to decide whether to play another round.
        # The input statement waits for the user to provide input, which is then stripped of leading/trailing whitespaces
        # and converted to lowercase for case-insensitive comparison.
        repeat_play = input("\n****play again?**** (press y or enter to continue): ").strip().lower()
        # Check if the player wants to play again by examining the entered input.
        # If the input is 'y', 'yes', or an empty string (Enter key pressed), proceed with another round.
        if repeat_play in ["y", "yes", ""]:
            # initiate another round by recursively calling the play_game function with the specified preference.
            play_game(player_name, preference)
        else:
            # Otherwise use sys.exit to gracefully terminate the program with a personalized goodbye message to the player.
            if __name__ == "__main__":
                sys.exit(f"👋 Thanks for playing my game, {player_name}! Byeeeee.\n" * 4)
            print(
                f"👋 Thanks for playing {'Rock, Paper, Scissors' if preference == 3 else 'Rock, Paper, Scissors, Lizard, Spock'}! See you next time.\n")
            return

    # Return the play_game function, creating a closure.
    # The play_game function retains access to the variables (__player_win__, __computer_win__, __tie__, __total__)
    # from its enclosing scope, allowing it to maintain and modify the game state across multiple calls.
    return play_game


# Main program
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2 and int(sys.argv[1]) in (3, 5):
            # Initialize the game
            fun_rps = game_init()

            # Get and validate player's name
            while True:
                name = input("👋 Welcome to my game! What's your name?\n").strip().title()
                if name:
                    print("")
                    break

            # 3 for classic 3 choice of Rock-Paper-Scissors,
            # 5 for improved 5 choice of Rock-Paper-Scissors-Lizard-Spock as chosen by player through command-line option
            fun_rps(name, int(sys.argv[1]))

        else:
            print(
                "Need an argument for initialization: \n3 for Rock, Paper, Scissors \n5 for Rock, Paper, Scissors, Lizard, Spock\n")
            sys.exit(1)
            sys.exit(
    except ValueError:
        sys.exit(
            "Need argument for initialization: \n3 for Rock, Paper, Scissors \n5 for Rock, Paper, Scissors, Lizard, Spock\n")



