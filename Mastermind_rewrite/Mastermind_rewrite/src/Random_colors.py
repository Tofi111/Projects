import random
from src.Colors import *

LENGTH = 6
MAX_ATTEMPTS = 20

def pick_random_colors(num_colors=LENGTH):
    all_colors = list(Color)

    selected_colors = random.sample(all_colors, num_colors)

    return selected_colors