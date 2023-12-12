import unittest
from unittest.mock import patch

from src.worldtime_raw_offset import get_response, get_raw_offset


class WorldTimeRawOffsetTests(unittest.TestCase):
    def test_get_response(self):
        result = get_response("london")

        self.assertEqual(result['raw_offset'], 0)

    def test_get_raw_offset_using_3_cities_from_a_list(self):
        citylist = ['London', 'Riga', 'Amsterdam']

        result = [get_raw_offset(city) for city in citylist]

        self.assertEqual(result, [0, 7200, 3600])

    