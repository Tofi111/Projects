import unittest
from unittest.mock import mock_open, patch

from src.Fetch_code_names import fetch_code_name


class fetchcodetests(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="US\nUTC\nEurope/London")
    def test_fetch_code_name_reads_file_correctly(self, mock_file_open):
        result = fetch_code_name()

        mock_file_open.assert_called_once_with('Timezones', 'r')

        self.assertEqual(result, ['US', 'UTC', 'Europe/London'])

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_fetch_code_name_handles_empty_file(self, mock_file_open):
        mock_file_open.return_value.read_data = ""

        result = fetch_code_name()

        mock_file_open.assert_called_once_with('Timezones', 'r')

        self.assertEqual(result, [])
