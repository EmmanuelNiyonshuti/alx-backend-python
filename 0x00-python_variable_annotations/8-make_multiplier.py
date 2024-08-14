#!/usr/bin/env python3
"""
implements a type-annoted function
that returns a function.
"""
from typing import Callable

multiply = Callable[[float], float]


def make_multiplier(multiplier: float) -> multiply:
    """
    returns a function.
    Args:
        multiplier (float)
    Return:
        a function.
    """
    def multiplication(multiplier: float) -> float:
        """
        multiplies two floats.
        Args:
            multiplier (float)
        Return:
            a product of two floats.
        """
        return multiplier * multiplier
    return multiplication
