"""
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number
of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not
possible to balance them.
"""

from linked_list_stack import Stack


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    n = len(input_string)
    if n % 2 != 0:
        return -1

    stack = Stack()
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            # If the subsequent one closes the previous one
            if stack.top() == "{" and bracket == "}":
                stack.pop()
            else:
                stack.push(bracket)

    cnt = 0
    while not stack.is_empty():
        cnt += [1, 2][int(stack.pop() == stack.pop())]
    return cnt


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = ["}}}}", 2]
    test_function(test_case_1)

    test_case_2 = ["}}{{", 2]
    test_function(test_case_2)

    test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
    test_function(test_case_1)

    test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
    test_function(test_case_2)

    test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
    test_function(test_case_3)
