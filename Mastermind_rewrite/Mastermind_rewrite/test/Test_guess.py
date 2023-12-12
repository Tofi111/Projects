import unittest
import parameterized
from src.Colors import Color
from src.Match_criteria import Match
from src.GameStatus import GameStatus
from collections import Counter
from src.guess_colors import guess

globals().update(Color.__members__)
globals().update(Match.__members__)
globals().update(GameStatus.__members__)


class Testguess(unittest.TestCase):
    @parameterized.parameterized.expand([
        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [EXACT] * 6),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, RED, RED, RED, RED, RED], [NO] * 6),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [PINK, ORANGE, YELLOW, GREEN, WHITE, BLUE], [MISMATCH] * 6),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, WHITE, GREEN],
         [EXACT] * 4 + [MISMATCH] * 2),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [PINK, YELLOW, ORANGE, BLUE, GREEN, WHITE],
         [EXACT] * 4 + [MISMATCH] * 2),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, WHITE, BLUE, GREEN],
         [EXACT] * 3 + [MISMATCH] * 3),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, PINK, CYAN, WHITE, BLUE, GREEN],
         [EXACT] + [MISMATCH] * 3 + [NO] + [NO]),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW],
         [EXACT] * 1 + [NO] * 5),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
         [EXACT] * 1 + [NO] * 5),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [PINK, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW],
         [MISMATCH] * 2 + [NO] * 4),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW],
         [MISMATCH] * 1 + [NO] * 5)

    ])
    def test_guess(self, selected_colors, user_provided_colors, response_expected):
        response = guess(selected_colors, user_provided_colors)

        actual_counts = Counter(response)

        expected_counts = Counter(response_expected)

        self.assertEqual(expected_counts, actual_counts)

    @parameterized.parameterized.expand([
        ([YELLOW, PINK, ORANGE, BLUE, GREEN, YELLOW],
         [ORANGE, YELLOW, BLUE, WHITE, PINK, GREEN],
         "Error: selected colors should be distinct"),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN],
         [ORANGE, YELLOW, BLUE, WHITE, PINK, GREEN],
         "Error: Expecting 6 selected colors"),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, RED],
         [ORANGE, YELLOW, BLUE, WHITE, PINK],
         "Error: Expecting 6 user provided colors"),
    ])
    def test_guess_invalid_input(self, selected_colors, user_provided_colors, error_message):
        with self.assertRaisesRegex(Exception, error_message):
            guess(selected_colors, user_provided_colors)
