#!/usr/bin/env python3
"""
Implements a coroutine that collects 10 random numbers
from another coroutine using async comprehension.
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    collects a list of random numbers using async comprehension.
    Return:
        a list of random numbers.
    """
    result = [i async for i in async_generator()]
    return result
