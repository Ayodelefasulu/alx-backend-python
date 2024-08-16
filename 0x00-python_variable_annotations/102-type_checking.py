#!/usr/bin/env python3
"""
This module defines a function `zoom_array` accepts tuple of integers
and integer as arguments, and returns a list of integer.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into a tuple by repeating each element a given number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be zoomed.
        factor (int): The number of times to repeat each element.

    Returns:
        List[int]: A list with each element of the tuple repeated.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
