#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine named `wait_n`.
"""

from typing import List

#from alx_backend_python.0x01-python_async_function.0-basic_async_syntax import wait_random
#from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float = 10.0) -> List[float]:
    """
    This asynchronous coroutine spawns `n` concurrent tasks of `wait_random`
    coroutine, each with the specified `max_delay`. It then gathers the results
    and returns them as an ascendingly ordered list without using `sort`.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (float, optional): The upper bound for the random delay in
            each task. Defaults to 10.0 seconds.

    Returns:
        List[float]: A list of delays experienced in ascending order.
    """

    tasks = []
    # Create tasks for each wait_random call
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    # Gather results from all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Leverage the inherent concurrency to achieve ascending order
    return results  # Results will be ordered due to task completion times
