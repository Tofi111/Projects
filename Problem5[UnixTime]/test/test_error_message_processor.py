import unittest
from unittest.mock import patch

from src.Error_message_processor import get_error_message
from src.UnixTime_information import *

class unixtimeinformationtest(unittest.TestCase):
    @patch('src.UnixTime_information.requests.get')
    def test_get_response(self, mock_get):
        expected_response = "Some error message from the URL"
        mock_get.return_value.text = expected_response

        mock_get.side_effect = Exception(f"Error: {expected_response}")

        with self.assertRaisesRegex(Exception, expected_response):
            get_response()

    def test_get_error_message(self):
        error_message = get_error_message("Some error message")

        self.assertEqual(error_message, "Error: Some error message")

