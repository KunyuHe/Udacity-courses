"""
Reverse Polish notation, also referred to as Polish postfix notation is a way of
laying out operators and operands.

When making mathematical expressions, we typically put arithmetic operators
(like +, -, *, and /) between operands. For example: 5 + 7 - 3 * 8

However, in Reverse Polish Notation, the operators come after the operands.
For example: 3 1 + 4 *

The above expression would be evaluated as (3 + 1) * 4 = 16

The goal of this exercise is to create a function that does the following:

Given a postfix expression as input, evaluate and return the correct final
answer.
Note: In Python 3, the division operator / is used to perform float division.
So for this problem, you should use int() after every division to convert the
answer to an integer.
"""

import operator

from linked_list_stack import Stack


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()
    char_operator = {"+": operator.add,
                     "-": operator.sub,
                     "/": operator.truediv,
                     "*": operator.mul}

    for char in input_list:
        if char in char_operator:
            b = stack.pop()
            a = stack.pop()
            stack.push(int(char_operator[char](a, b)))
        else:
            stack.push(int(char))

    return stack.pop()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [["3", "1", "+", "4", "*"], 16]
    test_function(test_case_1)

    test_case_2 = [["4", "13", "5", "/", "+"], 6]
    test_function(test_case_2)

    test_case_3 = [
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        22]
    test_function(test_case_3)
