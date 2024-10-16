#!/usr/bin/env python3
"""function which takes a list of int and floats and returns sum as a float."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum of mixed type list (int & float)
    :param mxd_lst: list of integer and float
    :return: sum of the mxd_lst as float
    """
    result: float = 0
    for e in mxd_lst:
        result += e
    return result
