#!/usr/bin/env python3
"""
implements a type-annoted function
that returns a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function.
    Args:
        multiplier (float)
    Return:
        a function.
    """
    def multiplication(x: float) -> float:
        """
        multiplies two floats.
        Args:
            multiplier (float)
        Return:
            a product of two floats.
        """
        return multiplier * x
    return multiplication
