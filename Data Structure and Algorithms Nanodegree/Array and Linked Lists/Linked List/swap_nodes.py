"""
Given a linked list, swap the two nodes present at position i and j, assuming
0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9
"""

from node import Node


def swap_nodes(head, i, j):
    """
    :param: head- head of input linked list
    :param: `position_one` - indicates position (index) ONE
    :param: `position_two` - indicates position (index) TWO
    return: head of updated linked list with nodes swapped

    TODO: complete this function and swap nodes present at position_one and
    position_two
    Do not create a new linked list
    """
    if i == j:
        return head

    curr1, prev1 = None, None
    curr2, prev2 = None, None
    curr, curr_idx = head, 0

    # Find the relevant nodes
    while curr is not None:
        if curr_idx == i:
            curr1 = curr
        elif curr_idx == j:
            curr2 = curr
            # assuming 0 <= i <= j
            break

        if curr1 is None:
            prev1 = curr
        prev2 = curr

        curr = curr.next
        curr_idx += 1

    prev2.next = curr1
    curr1.next, curr2.next = curr2.next, curr1.next
    # If the node at first index is the head
    if prev1 is None:
        head = curr2
    else:
        prev1.next = curr2
    return head


def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")


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
        print(head.value, end=" ")
        head = head.next
    print()


if __name__ == '__main__':
    arr = [3, 4, 5, 2, 6, 1, 9]
    head = create_linked_list(arr)
    left_index = 3
    right_index = 4
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 2
    right_index = 4
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 0
    right_index = 1
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)
