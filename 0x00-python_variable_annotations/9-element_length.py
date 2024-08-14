#!/usr/bin/env python3
"""
Module for working with sequences and their lengths.

This module provides a function
to calculate the length of each sequence in an iterable
of sequences,
returning a list of tuples with the sequence and its length.
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
                                (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
                        each containing a sequence from `lst`
                        and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
