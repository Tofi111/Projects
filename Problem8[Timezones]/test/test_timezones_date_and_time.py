import datetime
import unittest
from unittest.mock import patch

from src.Timezones_date_and_time import get_response, get_time, parse_response, get_date


class TimeAndDateTests(unittest.TestCase):
    @patch('src.Timezones_date_and_time.get_response')
    def test_get_response(self, mock_get_response):
        mock_get_response.return_value = {'$id': '1'}

        result = get_response('est')

        self.assertEqual(result['$id'], '1')

    @patch('src.Timezones_date_and_time.get_response')
    def test_parse_response(self, mock_get_response):
        mock_get_response.return_value = {'currentDateTime': '2023-11-26T22:11-05:00'}

        result = parse_response('est')

        self.assertEqual(result, datetime.datetime(2023, 11, 26, 22, 11, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))))

    @patch('src.Timezones_date_and_time.get_response')
    def test_get_time(self, mock_get_response):
        mock_get_response.return_value = {'currentDateTime': '2023-11-26T22:11-05:00'}

        result = get_time('est')

        self.assertEqual(result, '22:11')

    @patch('src.Timezones_date_and_time.get_response')
    def test_get_date(self, mock_get_response):
        mock_get_response.return_value = {'currentDateTime': '2023-11-26T22:11-05:00'}

        result = get_date('est')

        self.assertEqual(result, '2023-11-26')


    @patch('src.Timezones_date_and_time.get_response')
    def test_get_date_throws_exception_if_service_returns_access_error(self, mock_get_response):
        code = 'est'

        mock_get_response.side_effect = ValueError(f"{code} Error: getting date for code")

        with self.assertRaisesRegex(ValueError, f"{code} Error: getting date for code"):
            get_date('est')

    @patch('src.Timezones_date_and_time.get_response')
    def test_get_time_throws_exception_if_service_returns_access_error(self, mock_get_response):
        code = 'est'

        mock_get_response.side_effect = ValueError(f"{code} Error: getting time for code")

        with self.assertRaisesRegex(ValueError, f"{code} Error: getting time for code"):
            get_time('est')

    @patch('src.Timezones_date_and_time.get_response')
    def test_parse_response_throws_exception_if_service_returns_access_error(self, mock_get_response):
        code = 'pdt'

        mock_get_response.side_effect = ValueError(f"{code} Error: invalid timezone code")

        with self.assertRaisesRegex(ValueError, f"{code} Error: invalid timezone code"):
            parse_response('pdt')
