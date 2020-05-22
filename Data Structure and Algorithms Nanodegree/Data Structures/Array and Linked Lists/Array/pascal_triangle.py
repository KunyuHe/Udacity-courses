"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is
0-based.

For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle:
https://www.mathsisfun.com/pascals-triangle.html
"""

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    curr_row, curr_len = [1], 1

    while n > 0:
        # Update current row
        new_row = []
        for i in range(curr_len + 1):
            if i == 0 or i == curr_len:
                new_row.append(1)
            else:
                new_row.append(curr_row[i-1] + curr_row[i])
        curr_row, curr_len = new_row, len(new_row)
        n -= 1

    return curr_row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    n = 0
    solution = [1]

    test_case = [n, solution]
    test_function(test_case)

    n = 1
    solution = [1, 1]

    test_case = [n, solution]
    test_function(test_case)

    n = 2
    solution = [1, 2, 1]

    test_case = [n, solution]
    test_function(test_case)

    n = 3
    solution = [1, 3, 3, 1]

    test_case = [n, solution]
    test_function(test_case)

    n = 4
    solution = [1, 4, 6, 4, 1]

    test_case = [n, solution]
    test_function(test_case)
