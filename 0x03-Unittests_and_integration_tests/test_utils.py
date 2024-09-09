#!/usr/bin/env python3
"""unit tests for access_nested_map function """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for testing the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, sequence, expected):
        """ tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, sequence), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, sequence, expected):
        """ """
        # self.assertRaises(KeyError, access_nested_map, nested_map, sequence)
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, sequence), expected


class TestGetJson(unittest.TestCase):
    """ """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """ """
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload

        mock_get_json.return_value = mock_resp

        res = get_json(test_url)
        print(res)
        mock_get_json.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)
