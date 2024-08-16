#!/usr/bin/env python3
"""
This module defines a function `to_kv` that takes a string and an
integer or float, and returns a tuple. The first element of the
tuple is the string, and the second element is the square of the
integer or float, annotated as a float.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of an integer or float.

    Args:
        k (str): A string to be the first element of the tuple.
        v (Union[int, float]): integer or float to be squared,
                               used as 2nd element.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
                        and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
