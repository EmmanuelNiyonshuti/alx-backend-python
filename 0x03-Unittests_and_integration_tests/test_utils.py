#!/usr/bin/env python3
"""unit tests for access_nested_map function """
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
