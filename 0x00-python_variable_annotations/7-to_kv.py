#!/usr/bin/env python3
"""
implements a type-annotated function
that returns a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a numeric value.

    Args:
        k (str): The string to be included in the tuple.
        v (Union[int, float]): The numeric value to be squared.
    Returns:
        Tuple[str, float]: A tuple where the first element
        is the string `k`, and the second element
        is the square of `v` as a float.
    """
    return (k, v**2)
