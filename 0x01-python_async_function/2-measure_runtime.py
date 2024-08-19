#!/usr/bin/env python3
"""
implements a function that measures the total execution time for a coroutine.
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time.
    Args:
        n (int)
        max_delay (int)
    Returns:
        The total execution time of wait_n coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time
    return elapsed / n
