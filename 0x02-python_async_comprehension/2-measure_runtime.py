#!/usr/bin/env python3
"""
This function executes async_comprehension four times
in parallel using asyncio.gather.
"""
import asyncio
import time
from typing import List
# from async_comprehension import async_comprehension
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()  # Start measuring time

    # Execute async_comprehension four times concurrently
    await asyncio.gather(
        async_c(),
        async_c(),
        async_c(),
        async_c()
    )

    end_time = time.time()  # End measuring time
    return end_time - start_time
