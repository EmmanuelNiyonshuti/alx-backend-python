#!/usr/bin/env python3
"""
defines a type-annotated function
that returns a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum up a list of floats.
    Args:
        input_list (list) - a list of floats.
    Return:
        sum of elements in the list as a float.
    """
    sum = 0
    for i in input_list:
        sum += i
    return float(sum)
