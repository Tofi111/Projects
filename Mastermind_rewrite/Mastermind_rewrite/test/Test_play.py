import unittest
import parameterized
from src.Colors import Color
from src.Match_criteria import Match
from src.GameStatus import GameStatus
from src.Play import play

globals().update(Color.__members__)
globals().update(Match.__members__)
globals().update(GameStatus.__members__)


class PlayTests(unittest.TestCase):
    @parameterized.parameterized.expand([
        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE],
         (GameStatus.WON, [Match.EXACT] * 6), 1),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, RED, RED, RED, RED, RED], (GameStatus.WRONG_GUESS, [NO] * 6),
         1),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, WHITE, GREEN],
         (GameStatus.WRONG_GUESS, [Match.EXACT] * 4 + [Match.MISMATCH] * 2), 1),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE],
         (GameStatus.WON, [Match.EXACT] * 6), 2),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, RED, RED, RED, RED, RED], (GameStatus.WRONG_GUESS, [NO] * 6),
         2),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE],
         (GameStatus.WON, [Match.EXACT] * 6), 20),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, RED, RED, RED, RED, RED], (GameStatus.LOST_GAME, [NO] * 6),
         20),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE],
         (GameStatus.LOST_GAME, [Match.EXACT] * 6), 21),

        ([YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE], [RED, RED, RED, RED, RED, RED], (GameStatus.LOST_GAME,
                                                                                      [NO] * 6), 21)

    ])
    def test_play(self, selected_colors, user_provided_colors, expected_result, num_attempt):

        if num_attempt > 20:
            with self.assertRaisesRegex(Exception, "Too many attempts"):
                play(selected_colors, user_provided_colors, num_attempt)

        else:
            self.assertEqual(expected_result, play(selected_colors, user_provided_colors, num_attempt))

    @parameterized.parameterized.expand([
        ([YELLOW, PINK, ORANGE, BLUE, GREEN],
         [ORANGE, YELLOW, BLUE, WHITE, PINK, GREEN],
         "Error: Expecting 6 selected colors", 1)
    ])
    def test_play_invalid_input(self, selected_colors, user_provided_colors, error_message, attempts):
        with self.assertRaisesRegex(Exception, error_message):
            play(selected_colors, user_provided_colors, attempts)
