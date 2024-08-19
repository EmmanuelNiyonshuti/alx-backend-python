#!/usr/bin/env python3
"""
implements a basic asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that wait for a random delay and returns it.
    Args:
        max_delay (int)
    Return:
        a float random number.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
