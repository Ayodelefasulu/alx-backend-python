#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that takes a float multiplier
and returns a function that multiplies a given float by the multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        its product with `multiplier`.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
