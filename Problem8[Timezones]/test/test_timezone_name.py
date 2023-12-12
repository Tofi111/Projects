import datetime
import unittest
from unittest.mock import patch

from src.Timezones_name import get_response, get_timezone_name


class TimeAndDateTests(unittest.TestCase):
    @patch('src.Timezones_date_and_time.get_response')
    def test_get_response(self, mock_get_response):
        mock_get_response.return_value = {'$id': '1'}

        result = get_response('est')

        self.assertEqual(result['$id'], '1')

    @patch('src.Timezones_date_and_time.get_response')
    def test_get_timezone_name(self, mock_get_response):
        mock_get_response.return_value = {'Eastern Standard Time'}

        result = get_timezone_name('est')

        self.assertEqual(result, 'Eastern Standard Time')
