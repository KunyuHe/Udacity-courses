"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
"""

from singly_linked_list import LinkedList


def even_after_odd(llist):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if llist.head.value is None:
        return llist

    even = LinkedList()
    odd = LinkedList()
    curr = llist.head

    while curr is not None:
        if curr.value % 2 == 0:
            even.append(curr.value)
        else:
            odd.append(curr.value)
        curr = curr.next

    curr = odd.head
    if curr is None:
        return even
    while curr.next is not None:
        curr = curr.next
    curr.next = even.head
    return odd


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    solution = [1, 3, 5, 2, 4, 6]

    llist = LinkedList().from_list(arr)
    res = even_after_odd(llist).to_list()

    for i, num in enumerate(solution):
        assert num == res[i]

    arr = [1, 3, 5, 7]
    solution = [1, 3, 5, 7]

    llist = LinkedList().from_list(arr)
    res = even_after_odd(llist).to_list()

    for i, num in enumerate(solution):
        assert num == res[i]
