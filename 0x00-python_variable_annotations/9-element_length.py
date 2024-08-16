#!/usr/bin/env python3
"""
This module defines a funct `element_length` that takes iterable of sequences
and returns a list of tuples, each containing a sequence and its length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each sequence in the input iterable.

    Args:
        lst (Iterable[Sequence]): iterable of sequences (e.g., lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
