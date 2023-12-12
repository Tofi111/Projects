import random
from src.Match_criteria import *

SPACE = ' '
NEW_LINE = '\n'

LENGTH = 6
MAX_ATTEMPTS = 20


def guess(selected_colors, user_provided_colors):
    check_selected_colors_is_unique(selected_colors)

    check_colors_size(selected_colors, f"Error: Expecting {LENGTH} selected colors")

    check_colors_size(user_provided_colors, f"Error: Expecting {LENGTH} user provided colors")

    response = lambda i: (Match.EXACT if selected_colors[i] == user_provided_colors[i] else
                          Match.MISMATCH if selected_colors[i] in user_provided_colors else Match.NO)

    return sorted([response(i) for i in range(LENGTH)], key=lambda match: match.value)


def check_selected_colors_is_unique(selected_colors):
    if len(selected_colors) != len(set(selected_colors)):
        raise Exception("Error: selected colors should be distinct")

def check_colors_size(colors, error_message):
    if len(colors) < LENGTH:
        raise Exception(error_message)

