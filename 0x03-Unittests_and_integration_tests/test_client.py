#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_url: str, mock_get_json: patch):
        """Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"repos_url": "fake_url"}

        # Call the method
        result = client.org

        # Check that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Check the returned value
        self.assertEqual(result, {"repos_url": "fake_url"})


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class.
    """

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """Test that GithubOrgClient._public_repos_url returns the correct URL.
        """
        org_name = "google"
        client = GithubOrgClient(org_name)

        # Mock data
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"}
        mock_get_json.return_value = mock_payload

        # Ensure the org method is called
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/google/repos")

        # Verify that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google")


if __name__ == "__main__":
    unittest.main()
