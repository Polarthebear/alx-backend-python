#!/usr/bin/env python3
"""
measure_time function with integers as args
measuring total execution time and returning
total_time / n
"""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Recording start time"""
    start_time = time.time()
    """wait_n called and wait for completion"""
    await wait_n(n, max_delay)
    """recording end time"""
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
