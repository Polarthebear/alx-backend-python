#!/usr/bin/env python3
"""
Measure_runtime coroutine that executes async_comprehension
four times in parallel using asyncio.gather
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    """
    timer_start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    timer_end = time.time()
    return timer_end - timer_start
