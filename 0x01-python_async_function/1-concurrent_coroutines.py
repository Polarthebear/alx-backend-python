#!/usr/bin/env python3
"""
wait_random import, with async routine taking 2 args
returning list of all delays.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """List of tasks running wait_random n times"""
    tasks = [asyncio.create_task(wait_random(max_delay))
             for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
