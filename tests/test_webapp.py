import unittest
from unittest import mock
from webapp import webapp

class TestWebapp(unittest.TestCase):

    @mock.patch("webapp.forismatic.get_quote", return_value="Test quote")
    @mock.patch("webapp.picsum.get_picture", return_value="Test picture")
    def test_index(self, mock_get_picture, mock_get_quote):
        with webapp.test_client() as client:
            response = client.post('/', data={'key': '123456', 'grayscale': '1'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test quote', response.data)
            self.assertIn(b'Test picture', response.data)

if __name__ == '__main__':
    unittest.main()