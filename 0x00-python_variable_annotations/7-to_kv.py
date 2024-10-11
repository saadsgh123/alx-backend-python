#!/usr/bin/env python3
"""module of a single function that convert key and value to tuple"""
import math
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Covert key and value to tuple
    :param k: key
    :param v: value
    :return: tuple
    """
    return k, math.pow(v, 2)
