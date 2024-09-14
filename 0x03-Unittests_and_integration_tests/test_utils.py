#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map.
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Ensure that the exception message is as expected
        self.assertEqual(context.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """Test that get_json returns expected result with mocked HTTP calls.
        """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Set up the mock to return a specific response
            mock_response = unittest.mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function under test
            result = get_json(test_url)

            # Assert that the result matches the expected payload
            self.assertEqual(result, test_payload)

            # Assert that requests.get was called exactly once with the
            # test_url
            mock_get.assert_called_once_with(test_url)

            # Reset mock for next iteration
            mock_get.reset_mock()


if __name__ == "__main__":
    unittest.main()
