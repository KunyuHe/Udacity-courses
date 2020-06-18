from typing import List, Tuple, Union

from numpy import Inf


def get_min_max(ints: List[int]) -> Union[Tuple[int, int], None]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not all([isinstance(num, int) for num in ints]):
        raise TypeError("Input list should be an array of integers.")

    if not ints:
        return

    min_ele, max_ele = Inf, -1 * Inf
    for ele in ints:
        if ele < min_ele:
            min_ele = ele
        if ele > max_ele:
            max_ele = ele

    return min_ele, max_ele
