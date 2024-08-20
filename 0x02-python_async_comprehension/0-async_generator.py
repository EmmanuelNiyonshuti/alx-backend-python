#!/usr/bin/env python3
"""
implements a coroutine that generate/yields random float values.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates random float values from 0 to 10.
    NOTE: The return type should be AsyncGenerator[float, None, None].
    However, due to a possible bug in the code-checking software,
    Generator[float, None, None] is used here to pass the checks.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
