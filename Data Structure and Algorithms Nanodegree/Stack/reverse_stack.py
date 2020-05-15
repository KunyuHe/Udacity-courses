"""
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at
the bottom), after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1
at the top).
"""

from linked_list_stack import Stack


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    holder = Stack()
    while not stack.is_empty():
        holder.push(stack.pop())
    return holder


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4]
    test_function(test_case_1)

    test_case_2 = [1]
    test_function(test_case_2)
