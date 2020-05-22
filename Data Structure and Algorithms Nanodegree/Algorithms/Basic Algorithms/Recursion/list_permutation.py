import copy


def permute(inputList):
    permutations = []

    if len(inputList) == 0:
        permutations.append([])

    else:
        sub = permute(inputList[1:])

        # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList)
        # in each sub_compoundList
        for lst in sub:
            for j in range(0, len(lst) + 1):
                permuted = copy.deepcopy(lst)
                permuted.insert(j, inputList[0])
                permutations.append(permuted)

    return permutations


def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


if __name__ == '__main__':
    print("Pass" if (check_output(permute([]), [[]])) else "Fail")
    print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
    print(
        "Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
    print("Pass" if (check_output(permute([0, 1, 2]),
                                  [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0],
                                   [2, 0, 1], [2, 1, 0]])) else "Fail")
