import unittest
import json
from what_is_year_now import what_is_year_now
from unittest.mock import patch


class TestWhatYearIsNow(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_what_year_is_now1(self, mock_object):
        response = {'currentDateTime': '2020-04-25T09:12:32.789345+03:00'}
        mock_object.return_value.__enter__.return_value.read.return_value \
            = json.dumps(response)
        self.assertEqual(what_is_year_now(), 2020)

    @patch('urllib.request.urlopen')
    def test_what_year_is_now2(self, mock_object):
        response = {'currentDateTime': '25.04.2020 09:12:32'}
        mock_object.return_value.__enter__.return_value.read.return_value \
            = json.dumps(response)
        self.assertEqual(what_is_year_now(), 2020)

    @patch('urllib.request.urlopen')
    def test_what_year_is_now3(self, mock_object):
        response = {'currentDateTime': '25/04/2020 09:12:32'}
        mock_object.return_value.__enter__.return_value.read.return_value \
            = json.dumps(response)
        with self.assertRaises(ValueError):
            what_is_year_now()
