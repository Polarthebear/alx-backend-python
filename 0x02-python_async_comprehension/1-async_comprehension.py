#!/usr/bin/env python3
"""
async_comprehension coroutine that collects 10 random numbers
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension coroutine that collects 10 random numbers"""
    return [obj async for obj in async_generator()]
