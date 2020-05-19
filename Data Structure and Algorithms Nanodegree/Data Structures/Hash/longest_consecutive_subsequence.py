"""
Problem Statement
Given a list of integers that contain natural numbers in random order. Write a
program to find the longest possible sub sequence of consecutive numbers in the
array. Return this subsequence in sorted order.

In other words, you have to return the sorted longest (sub) list of consecutive
numbers present anywhere in the given list.

For example, given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2,
3, 4, 5

Note
The solution must take O(n) time. Can you think of using a dictionary here?
If two subsequences are of equal length, return the subsequence whose index of
smallest element comes first.
"""


def longest_consecutive_subsequence(arr):
    arr, included = set(arr), set()
    longest_seq = []

    for num in arr:
        if num in included or (num - 1) in arr:
            continue

        curr, seq = num, []
        while curr in arr:
            seq.append(curr)
            included.add(curr)
            curr += 1

        if len(seq) > len(longest_seq) or (len(seq) == len(longest_seq) and
                                           seq[0] < longest_seq[0]):
            longest_seq = seq[:]

    return longest_seq


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
    test_function(test_case_1)

    test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6],
                   [8, 9, 10, 11, 12]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    test_function(test_case_3)
