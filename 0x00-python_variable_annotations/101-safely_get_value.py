#!/usr/bin/env python3
"""
This module defines a function `safely_get_value` that retrieves a value
from a dictionary given a key, or returns a default value if the key is
not present.
"""

from typing import Mapping, TypeVar, Any, Union

K = TypeVar('K')
V = TypeVar('V')
T = TypeVar('T', bound=V)


def safely_get_value(
    dct: Mapping[K, V],
    key: K,
    default: Union[V, None] = None
) -> Union[V, T]:
    """
    Retrieve the value associated with a key from a dictionary,
    or return a default value.

    Args:
        dct (Mapping[K, V]): The dictionary to search.
        key (K): The key to look up in the dictionary.
        default (Union[V, None]): Default value to return if key isn't found.

    Returns:
        Union[V, T]: The value associated with the key if it exists,
                     otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
