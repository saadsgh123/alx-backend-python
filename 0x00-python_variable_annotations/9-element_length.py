#!/usr/bin/env python3
"""
module contain a single function which
return the length of an iterable sequence list
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the  length of an iterable sequence list
    :param lst: iterable list
    :return: tuple contain the length of the list
    """
    return [(i, len(i)) for i in lst]
