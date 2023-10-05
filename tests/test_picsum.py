import unittest
from unittest import mock
import picsum


class TestPicsum(unittest.TestCase):

    @mock.patch("picsum.API_URL", "https://httpbin.org/status/404")
    def test_picsum_unavailable(self):
        image_data = picsum.get_picture(grayscale=False, cli=True)
        self.assertEqual(image_data, None)

    def test_picsum_api_url(self):
        api_url = picsum.get_api_url(grayscale=True)
        self.assertEqual(api_url, "https://picsum.photos/512/384?grayscale")

    def test_get_picture(self):
        # Test that the function returns a non-empty string
        self.assertTrue(len(picsum.get_picture()) > 0)

    def test_get_grayscale_picture(self):
        # Test that the function returns a non-empty string when grayscale is True
        self.assertTrue(len(picsum.get_picture(grayscale=True)) > 0)

    def test_get_cli_picture(self):
        # Test that the function returns a non-empty string when cli is True
        self.assertTrue(len(picsum.get_picture(cli=True)) > 0)

if __name__ == '__main__':
    unittest.main()