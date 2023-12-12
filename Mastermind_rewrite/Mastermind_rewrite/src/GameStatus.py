from enum import Enum
from src.Match_criteria import *
class GameStatus(Enum):
    WON = 1
    WRONG_GUESS = 2
    LOST_GAME = 3

LENGTH = 6
MAX_ATTEMPTS = 20

def determine_game_status(response, attempts):
    if is_exact_match(response) and is_within_attempt_limit(attempts):
        return GameStatus.WON

    elif has_mismatch_or_no_match(response) and is_within_attempt_limit(attempts):
        return GameStatus.WRONG_GUESS

    else:
        return GameStatus.LOST_GAME


def is_exact_match(response):
    return all(match == Match.EXACT for match in response)


def has_mismatch_or_no_match(response):
    return any(match in {Match.MISMATCH, Match.NO} for match in response)


def is_within_attempt_limit(attempts):
    return attempts <= MAX_ATTEMPTS
