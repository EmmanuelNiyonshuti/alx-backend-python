#!/usr/bin/env python3
"""
implements a type-annotated function
that returns a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    computes the sum of a list of integers and floats.
    Args:
        mxd_lst (list) - a list of integers and floats.
    Return:
        a sum as a float.
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return float(sum)
