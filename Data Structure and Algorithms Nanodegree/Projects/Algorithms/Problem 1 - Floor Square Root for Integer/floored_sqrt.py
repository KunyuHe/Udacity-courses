from typing import Union


def sqrt(number: int) -> Union[int, None]:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return

    if number == 0 or number == 1:
        return number

    # Floored square root of a natural number (starting from 2) is half or less
    start, end = 0, number // 2
    while end >= start:
        middle = (start + end) // 2
        middle_sq = middle * middle

        if middle_sq == number:
            return middle
        if middle_sq < number:
            start = middle + 1
        else:
            end = middle - 1
    else:
        return middle
