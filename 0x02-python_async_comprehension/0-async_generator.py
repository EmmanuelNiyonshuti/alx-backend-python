#!/usr/bin/env python3
"""
implements a coroutine that generate/yields random float values.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generates random float values from 0 to 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
