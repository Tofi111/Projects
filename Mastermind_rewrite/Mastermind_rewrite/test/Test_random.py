import unittest
import parameterized
from src.Colors import Color
from src.Match_criteria import Match
from src.GameStatus import GameStatus
from src.Random_colors import pick_random_colors
from src.Play import LENGTH

globals().update(Color.__members__)
globals().update(Match.__members__)
globals().update(GameStatus.__members__)


class RandomTests(unittest.TestCase):
    def test_random_colors_are_random(self):
        selected_colors = pick_random_colors(LENGTH)

        self.assertEqual(len(selected_colors), LENGTH)

        for color in selected_colors:
            self.assertTrue(isinstance(color, Color))

        self.assertNotEqual(selected_colors, list(Color))
