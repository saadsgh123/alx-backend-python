#!/usr/bin/env python3
"""
module that contain a single function that takes a
float multiplier as argument and
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that multiplies a float by multiplier.
    :param multiplier: float
    :return: a callable function
    """
    def square(n: float) -> float:
        return multiplier * n

    return square
