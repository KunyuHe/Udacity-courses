from typing import List

from typing_extensions import Literal


def sort_012(input_list: List[Literal[0, 1, 2]]):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not all([isinstance(digit, int) for digit in input_list]):
        raise TypeError("Elements in the input list should be integers.")

    if not all([digit in (0, 1, 2) for digit in input_list]):
        raise ValueError("Elements in the input list should be 0, 1, or 2.")

    digit_freq = [0 for _ in range(3)]
    for digit in input_list:
        digit_freq[digit] += 1

    res = []
    for digit, freq in enumerate(digit_freq):
        res.extend([digit] * freq)

    return res
