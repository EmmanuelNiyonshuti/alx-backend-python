#!/usr/bin/env python3
"""
implements a function the returns an asyncio.Task
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates asyncio task object that runs the wait_random coroutine.
    Args:
        max_delay (int): The maximum delay in seconds for wait_random.
    Return:
        asyncio.Task: A Task object that represents
                    the execution of the wait_random coroutine.
    """
    return asyncio.Task(wait_random(max_delay))
