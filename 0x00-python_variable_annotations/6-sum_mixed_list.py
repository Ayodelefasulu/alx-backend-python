#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that takes a list of integers
and floats, and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): list containing integers & floats.

    Returns:
        float: The sum of the list, as a float.
    """
    return sum(mxd_lst)
