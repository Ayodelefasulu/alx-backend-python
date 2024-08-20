#!/usr/bin/env python3
"""
This module contains the wait_random coroutine which
waits for a random delay.
"""


import asyncio
import random
#from typing import Union


async def wait_random(max_delay = 10):
    """
    Waits for a random delay between 0 and
    max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds (10).

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
