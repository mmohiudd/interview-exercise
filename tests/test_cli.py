import unittest
from unittest import mock
from click.testing import CliRunner
from cli import cli

class TestCli(unittest.TestCase):
    @mock.patch("forismatic.get_quote", return_value="Test quote")
    @mock.patch("picsum.get_picture", return_value="Test picture")
    def test_cli(self, mock_get_picture, mock_get_quote):
        runner = CliRunner()
        result = runner.invoke(cli, ["--key", "123456", "--grayscale"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Test quote", result.output)
        self.assertIn("Test picture", result.output)
