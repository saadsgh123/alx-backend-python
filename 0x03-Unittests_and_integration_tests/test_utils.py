#!/usr/bin/env python3
"""
Test for access_nested_map function
"""
import unittest

from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """
        Tests the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
            Test the access_nested_map method.
            Args:
                nested_map (Dict): A dictionary that may have nested dictionaries
                path (List, tuple, set): Keys to get to the required value in the
                nested dictionary
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
