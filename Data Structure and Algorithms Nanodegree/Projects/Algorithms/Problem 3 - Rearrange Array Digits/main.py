from typing import List, Tuple, Union


def rearrange_digits(input_list: List[int]) -> Union[Tuple[int, int], None]:
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int), (int): Two maximum sums
    """
    if len(input_list) <= 1:
        raise ValueError("Input list should have more than one digit "
                         "for partition.")

    if not all([isinstance(digit, int) for digit in input_list]):
        raise TypeError("Elements in the input list should be integers.")

    if not all([(digit >= 0 and digit <= 9) for digit in input_list]):
        raise ValueError("Elements in the input list should be digits.")

    # List to host digit frequencies from 9 to 0
    freq_lst = [0 for _ in range(10)]

    for digit in input_list:
        freq_lst[9 - digit] += 1

    res = ["", ""]
    # Boolean to indicate the index to append the next digit
    i_append_flag = False
    for i, freq in enumerate(freq_lst):
        while freq > 0:
            res[int(i_append_flag)] += str(9 - i)
            i_append_flag = not i_append_flag
            freq -= 1

    return (int(res[0]), int(res[1]))
