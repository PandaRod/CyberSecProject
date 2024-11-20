import unittest
from unittest.mock import patch, Mock
from datetime import datetime
from main import feed_data, saint_algorithm  # Assuming main.py contains the refactored code


class TestFeedData(unittest.TestCase):
    def test_feed_data_geo(self):
        expected = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "29.886829786|-97.93666292",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
        }
        self.assertEqual(feed_data("geo"), expected)

    def test_feed_data_date(self):
        self.assertIsInstance(feed_data("date"), datetime)

    def test_feed_data_user(self):
        expected = {
            "action": "query",
            "meta": "userinfo",
            "uiprop": "rights",
            "format": "json"
        }
        self.assertEqual(feed_data("user"), expected)

    def test_feed_data_invalid(self):
        with self.assertRaises(ValueError):
            feed_data("invalid")


class TestSaintAlgorithm(unittest.TestCase):
    @patch("requests.Session.get")
    def test_saint_algorithm_geosearch(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"query": {"geosearch": []}}
        mock_get.return_value = mock_response

        result = saint_algorithm("geosearch")
        self.assertIn("query", result)
        self.assertIn("geosearch", result["query"])

    @patch("requests.Session.get")
    def test_saint_algorithm_user(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"query": {"userinfo": {}}}
        mock_get.return_value = mock_response

        result = saint_algorithm("user")
        self.assertIn("query", result)
        self.assertIn("userinfo", result["query"])

    def test_saint_algorithm_date(self):
        result = saint_algorithm("date")
        self.assertIsInstance(result, datetime)

    def test_saint_algorithm_invalid(self):
        with self.assertRaises(ValueError):
            saint_algorithm("invalid")


if __name__ == '__main__':
    unittest.main()
