from typing import List


def _search(arr: List[int], num: int, i_start: int, i_end: int) -> int:
    if i_start > i_end:
        return -1

    i_mid = (i_start + i_end) // 2
    start, mid, end = arr[i_start], arr[i_mid], arr[i_end]
    if mid == num:
        return i_mid

    # Left half sorted
    if start <= mid:
        # If key is in the left half
        if (start <= num and mid >= num):
            return _search(arr, num, i_start, i_mid - 1)
        # Else, key is in the right half
        return _search(arr, num, i_mid + 1, i_end)
    # Right half sorted
    if (mid <= num and end >= num):
        return _search(arr, num, i_mid + 1, i_end)
    return _search(arr, num, i_start, i_mid - 1)


def search(input_list: List[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not all([isinstance(num, int) for num in input_list]):
        raise TypeError("Input list should be an array of integers.")

    if not isinstance(number, int):
        raise TypeError("The target number should be an integer.")

    return _search(input_list, number, 0, len(input_list) - 1)
