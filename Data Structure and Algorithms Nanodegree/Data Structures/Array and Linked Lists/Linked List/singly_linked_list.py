from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """
        Prepend a value to the beginning of the list.
        """
        self.head, self.head.next = Node(value), self.head

    def append(self, value):
        """
        Append a value to the end of the list.
        """
        if self.head is None:
            self.head = Node(value)
        else:
            # Move to the tail (the last node)
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(value)

    def from_list(self, arr):
        for num in arr:
            self.append(num)
        return self

    def to_list(self):
        return [value for value in self]

    def search(self, value):
        """
        Search the linked list for a node with the requested value and return
        the node.
        """
        curr = self.head

        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next

        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """
        Remove first occurrence of value.
        """
        if self.head is None:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return None

        curr = self.head

        while curr.next is not None:
            if curr.next.value == value:
                curr.next = curr.next.next
                return None
            curr = curr.next

        raise ValueError("Value not found in the list.")

    def pop(self):
        """
        Return the first node's value and remove it from the list.
        """
        curr = self.head
        self.head = self.head.next

        return curr.value

    def insert(self, value, pos):
        """
        Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list.
        """
        if self.head is None or pos == 0:
            self.prepend(value)
            return None

        prev, curr = self.head, self.head.next
        pos -= 1
        while pos > 0 and curr is not None:
            prev, curr = curr, curr.next
            pos -= 1
        prev.next = Node(value)
        prev.next.next = curr

    def size(self):
        """
        Return the size or length of the linked list.
        """
        return len(self.to_list())

    def reverse(self):
        """
        Reverse the linked list in place, see:
        https://www.geeksforgeeks.org/reverse-a-linked-list/
        """
        prev, curr, next = None, self.head, None

        while curr is not None:
            next = curr.next
            curr.next, prev = prev, curr
            curr = next
        self.head = prev

        return self

    def is_circular(self):
        if self.head is None:
            return False

        slow, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str(self.to_list())


if __name__ == '__main__':
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [
        1], f"list contents: {linked_list.to_list()}"

    # Test append - 1
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1,
                                     3], f"list contents: {linked_list.to_list()}"

    # Test append - 2
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [
        1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1,
                                     3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(
        1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(
        4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4,
                                     3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4,
                                     3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1,
                                     4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1,
                                     4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1,
                                     4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4,
                                     3], f"list contents: {linked_list.to_list()}"

    # Test reverse
    llist = LinkedList()
    for value in [4, 2, 5, 1, -3, 0]:
        llist.append(value)

    assert list(llist.reverse()) == list([0, -3, 1, 5, 2, 4])
    assert list(llist) == list(llist.reverse().reverse())
