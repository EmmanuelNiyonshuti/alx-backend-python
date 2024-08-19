#!/usr/bin/env python3
"""
implements a coroutine that performs a concurent operation.
"""
from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    Args:
        n (int) - Number of times wait_delay will be spawned.
        max_delay (int) - The max number of delay for wait_random.
    Return:
        list of all the delays(float values) in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    sorted_delays = []
    while delays:
        small_num = min(delays)
        sorted_delays.append(small_num)
        delays.remove(small_num)
    return sorted_delays
