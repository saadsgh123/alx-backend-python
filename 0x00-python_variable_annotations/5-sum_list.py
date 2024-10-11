#!/usr/bin/env python3
""" Contains a function that sums a list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    the sum of the elements in the list
    :param input_list: float numbers list
    :return: sum of input_list
    """
    result: float = 0
    for e in input_list:
        result += e
    return result
