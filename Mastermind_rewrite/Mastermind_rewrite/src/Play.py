from src.guess_colors import *
from src.GameStatus import *

LENGTH = 6
MAX_ATTEMPTS = 20
def validate_number_of_attempts(attempts):
    if attempts > MAX_ATTEMPTS:
        raise ValueError("Too many attempts")

def play(selected_colors, user_colors, attempts):
    validate_number_of_attempts(attempts)

    response = guess(selected_colors, user_colors)

    game_status = determine_game_status(response, attempts)

    return game_status, response
