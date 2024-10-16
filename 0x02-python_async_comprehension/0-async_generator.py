#!/usr/bin/env python3
"""
async_generator coroutine taking no args
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Define async generator coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
