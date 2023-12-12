from src.Colors import Color
from src.Play import play, MAX_ATTEMPTS
from src.Random_colors import pick_random_colors
from GameStatus import *


def main():
    selected_colors = pick_random_colors()

    print("Welcome to Mastermind!")
    print(f"Try to guess the 6 combination of colors. You have a maximum of {MAX_ATTEMPTS} attempts.")
    attempts(selected_colors)


def display_colors(colors):
    return ", ".join(color.name for color in colors)


def attempts(selected_colors):
    num_of_attempts = 0
    while num_of_attempts < MAX_ATTEMPTS:
        user_input = input(f"\nEnter your 6 color guesses separated by a space: ").upper()
        try:
            user_colors = [Color[color] for color in user_input.split()]
        except KeyError:
            print("Invalid color input. Please enter valid colors.")
            continue

        game_status, response = play(selected_colors, user_colors, num_of_attempts + 1)

        print(f"\nAttempt {num_of_attempts + 1}/{MAX_ATTEMPTS}:")
        print(f"Your guess: {display_colors(user_colors)}")
        print("Result: ", end="")

        Match_update(response)
        result = GameStatus_update(game_status, selected_colors)

        if result == "break":
            break
        else:
            num_of_attempts += 1


def Match_update(response):
    for match in response:
        if match == Match.EXACT:
            print("Black", end=" ")
        elif match == Match.MISMATCH:
            print("Silver", end=" ")
        else:
            print("-", end=" ")

    print()


def GameStatus_update(game_status, selected_colors):
    if game_status == GameStatus.WON:
        print("Congratulations! You've guessed the correct combination.")
        return "break"
    elif game_status == GameStatus.WRONG_GUESS:
        print("Sorry, you've run out of attempts. The correct combination was:", display_colors(selected_colors))
        return "break"
    else:
        return None


main()