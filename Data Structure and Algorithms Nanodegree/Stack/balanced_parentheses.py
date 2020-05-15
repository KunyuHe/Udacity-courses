"""
In this exercise you are going to apply what you learned about stacks with a
real world problem. We will be using stacks to make sure the parentheses are
balanced in mathematical expressions such as:  ((32+8)∗(5/2))/(2+6).  In real
life you can see this extend to many things such as text editor plugins and
interactive development environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or
False if it is not.

Try to code up a solution and pass the test cases.
"""

from pythonic_stack import Stack


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            # If no pairing ("
            if stack.pop() is None:
                return False
    return stack.is_empty()


if __name__ == '__main__':
    print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print("Pass" if not (
        equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
