#!/usr/bin/env python3
"""
Module for 100-safe_first_element
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
