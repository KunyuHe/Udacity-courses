"""
Problem Statement
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""

from node import Node


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    if i == 0:
        return None

    if head is None or j <= 0 or i < 0:
        return head

    curr, prev = head, None
    while curr is not None:
        # Skip i nodes
        for _ in range(i - 1):
            if curr is None:
                return head
            curr = curr.next
        prev, curr = curr, curr.next

        # Delete j nodes
        for _ in range(j):
            if curr is None:
                break
            curr = curr.next
        prev.next = curr

    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for value in arr[1:]:
        tail.next = Node(value)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.value, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.value != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 2
    head = create_linked_list(arr)
    solution = [1, 2, 5, 6, 9, 10]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 3
    head = create_linked_list(arr)
    solution = [1, 2, 6, 7, 11, 12]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 4
    head = create_linked_list(arr)
    solution = [1, 2]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 0
    head = create_linked_list(arr)
    solution = [1, 2, 3, 4, 5]
    test_case = [head, i, j, solution]
    test_function(test_case)
