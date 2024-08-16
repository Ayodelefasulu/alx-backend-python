#!/usr/bin/env python3
"""
This module defines a function `safe_first_element`
that returns the first element of a sequence if it exists,
or `None` if the sequence is empty.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a seq, or return None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A seq (e.g., list, tuple) of any type of elements.

    Returns:
        Union[Any, None]: First element of the seq or None if the seq is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
