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
