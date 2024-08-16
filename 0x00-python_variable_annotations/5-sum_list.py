#!/usr/bin/env python3
"""
This module defines a function `sum_list` that takes a list of floats
and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
