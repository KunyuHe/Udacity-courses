"""
Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
"""


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the
          string
    """
    return permuteString(string, 0)


def permuteString(string, idx):
    res = []

    if idx >= len(string):
        res.append("")
    else:
        sub = permuteString(string, idx + 1)
        add = string[idx]
        for base in sub:
            for idx in range(len(base) + 1):
                res.append(base[:idx] + add + base[idx:])

    return res


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    string = 'ab'
    solution = ['ab', 'ba']
    test_case = [string, solution]
    test_function(test_case)

    string = 'abc'
    output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    test_case = [string, output]
    test_function(test_case)

    string = 'abcd'
    output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda',
              'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca',
              'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
    test_case = [string, output]
    test_function(test_case)
