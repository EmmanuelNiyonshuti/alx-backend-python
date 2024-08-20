#!/usr/bin/env python3
"""
impements a coroutine that executes another coroutine
4 times in parallel and measures the run time.
"""
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        Measure the runtime of executing async_comprehension
        four times in parallel.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    elapsed = end - start
    return elapsed
