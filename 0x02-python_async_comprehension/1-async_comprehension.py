#!/usr/bin/env python3
"""
This asynchronous function uses sync comprehension
"""
import asyncio
from typing import List
#from .0-async_generator import async_generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously from
    async_generator using an async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]
