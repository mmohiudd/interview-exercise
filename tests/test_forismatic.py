import unittest
from unittest import mock
import forismatic


class TestForismatic(unittest.TestCase):
    @mock.patch("forismatic.API_URL", "https://httpbin.org/status/404")
    def test_forismatic_unavailable(self):
        quote = forismatic.get_quote()
        self.assertEqual(quote, None)

    def test_forismatic_api_url(self):
        api_url = forismatic.get_api_url(key=10)
        self.assertEqual(api_url, "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en&key=10")

    @mock.patch("forismatic.requests.get")
    def test_get_quote_response(self, mock_get):
        mock_get.return_value.json.return_value = {"quoteText": "Test quote"}
        quote = forismatic.get_quote()
        self.assertEqual(quote, "Test quote")

if __name__ == '__main__':
    unittest.main()