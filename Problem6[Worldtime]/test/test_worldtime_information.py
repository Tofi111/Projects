import unittest
from unittest.mock import patch

import requests

from src.Worldtime_information import get_raw_offset


class WorldTimeInformationTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_raw_offset_returns_raw_offset_data(self):
        raw_offset_data = lambda: (0)

        self.assertEqual(get_raw_offset(raw_offset_data), (0))

    def test_get_raw_offset_returns_network_error(self):
        raw_offset_data = lambda: exec('raise Exception("---")')

        self.assertEqual(get_raw_offset(raw_offset_data), "---")

    # @patch('src.Worldtime_information.get_raw_offset')
    # def test_get_raw_offset_request_exception(self, mock_get_raw_offset):
    #     mock_get_raw_offset.side_effect = requests.exceptions.RequestException("Mocked error")
    #
    #     result = get_raw_offset('ny')
    #
    #     self.assertEqual(result, 'ERR')
