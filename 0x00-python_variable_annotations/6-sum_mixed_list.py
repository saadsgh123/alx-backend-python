#!/usr/bin/env python3
"""function which takes a list of integers and floats and returns their sum as a float."""
from typing import Union


def sum_mixed_list(mxd_lst: Union[float, int]) -> float:
    """
    Sum of mixed type list (int & float)
    :param mxd_lst: list of integer and float
    :return: sum of the mxd_lst as float
    """
    result: float = 0
    for e in mxd_lst:
        result += e
    return result
