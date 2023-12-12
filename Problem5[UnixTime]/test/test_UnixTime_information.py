import unittest
from unittest.mock import patch

from src.UnixTime_information import *

class unixtimeinformationtest(unittest.TestCase):
    @patch('src.UnixTime_information.requests.get')
    def test_get_response(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.text = 'unixtime: 1700960037'

        mock_get.return_value = mock_response

        self.assertEqual(get_response(), mock_response.text)

    @patch('src.UnixTime_information.requests.get')
    def test_Unixtime_value(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.text = 'unixtime: 1700960037'

        mock_get.return_value = mock_response

        self.assertEqual(get_unixtime(), '1700960037')

