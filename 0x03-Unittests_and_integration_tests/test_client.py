#!/usr/bin/env python3
""" """
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import *
from utils import *


class TestGithubOrgClient(unittest.TestCase):
    """ Test Case for github client org"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ Test the GIthubClient.org returns the correct value.
        ensures that get_json is called once with the expected argument"""
        mock_get_json.return_value = {"is_verified": True}
        client = GithubOrgClient(org_name)
        res1 = client.org
        res2 = client.org
        mock_get_json.assert_called_once_with(client.ORG_URL.format(
            org=org_name))
        self.assertEqual(res1, {"is_verified": True})

    def test_public_repos_url(self):
        """ tesing a read only propert using `PropertyMock` """
        with patch.object(GithubOrgClient, "org",  new_callable=PropertyMock) \
                as mock:
            mock.return_value = {
                "repos_url":  "https://api.github.com/orgs/dummy/repos"
                }
            obj = GithubOrgClient("dummy")
            res = obj._public_repos_url
            self.assertEqual(res, "https://api.github.com/orgs/dummy/repos")

    @patch("client.get_json")
    @patch.object(
        GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """ Test the public repos method """
        repos_url = "https://api.github.com/orgs/dummy/repos"

        mock_public_repos_url.return_value = repos_url

        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache-2.0"}},
            {"name": "repo3", "license": {"key": "MIT"}}
        ]
        client = GithubOrgClient("dummy")
        res = client.public_repos(license="MIT")
        self.assertEqual(res, ["repo1", "repo3"])

        mock_get_json.assert_called_once_with(repos_url)
        mock_public_repos_url.assert_called_once()
