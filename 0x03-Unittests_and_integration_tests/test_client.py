#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient
import requests
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock)
    def test_public_repos(
            self,
            mock_public_repos_url: Mock,
            mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.public_repos returns the
           correct list of repos.

        Args:
            mock_public_repos_url (Mock): Mock obj for the
            _public_repos_url property.
            mock_get_json (Mock): Mock object for the get_json method.
        """
        org_name: str = "google"
        client: GithubOrgClient = GithubOrgClient(org_name)

        # Mock data
        expected_url: str = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = expected_url
        # mock_public_repos_url.return_value = \
        #    "https://api.github.com/orgs/google/repos"
        mock_payload: list[dict[str, dict[str, str]]] = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache-2.0"}},
            {"name": "repo3", "license": {"key": "MIT"}},
        ]

        # Mock the get_json method
        mock_get_json.return_value = mock_payload

        # Test the public_repos method
        repos: list[str] = client.public_repos(license="MIT")
        expected_repos: list[str] = ["repo1", "repo3"]
        self.assertEqual(repos, expected_repos)

        # Ensure get_json was called with the correct URL
        mock_get_json.assert_called_once_with(expected_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: dict,
            license_key: str,
            expected: bool) -> None:
        """Test that GithubOrgClient.has_license returns
           correct boolean based on repo and license_key.

        Args:
            repo (dict): A dictionary representing a repository.
            license_key (str): The license key to check for.
            expected (bool): The expected result.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

# Define a class to parameterize the test with different fixtures


@parameterized_class([{"org_payload": org_payload,
                       "repos_payload": repos_payload,
                       "expected_repos": expected_repos,
                       "apache2_repos": apache2_repos}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient's public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """Set up mock responses for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Configure mock to return the correct fixtures based on URL
        cls.mock_get.side_effect = cls.mock_get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get."""
        cls.get_patcher.stop()

    @classmethod
    def mock_get_side_effect(cls, url, *args, **kwargs):
        """Define the behavior of the mock based on URL."""
        if url == 'https://api.github.com/orgs/test_org':
            return Mock(json=lambda: cls.org_payload)
        elif url == 'https://api.github.com/orgs/test_org/repos':
            return Mock(json=lambda: cls.repos_payload)
        else:
            raise ValueError(f"Unexpected URL: {url}")

    def setUp(self):
        """Set up the GithubOrgClient instance for testing."""
        self.client = GithubOrgClient("test_org")

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient."""
        repos = self.client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_apache2_repos(self):
        """Test the Apache2 repositories method."""
        repos = self.client.public_repos()
        apache2_repos = self.client.apache2_repos()
        self.assertEqual(apache2_repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
