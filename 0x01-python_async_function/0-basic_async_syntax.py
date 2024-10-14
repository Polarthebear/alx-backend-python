#!/usr/bin/env python3
"""
Async coroutine that waits for delay
between 0 and max_delay seconds and returns it
"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Random float generated between 0 and max_delay"""
    delay = random.uniform(0, max_delay)

    """Asynchornously wait for rand delay"""
    await asyncio.sleep(delay)
    return delay
