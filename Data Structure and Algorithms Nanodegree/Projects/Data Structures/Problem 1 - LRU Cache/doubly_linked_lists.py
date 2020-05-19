from node import DoubleNode


class DoublyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def append(self, key, value):
        if self.head is None:
            self.prepend(key, value)
        else:
            self.tail.next = DoubleNode(key, value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.num_elements += 1

    def prepend(self, key, value):
        if self.head is None:
            self.head = DoubleNode(key, value)
            self.tail = self.head
        else:
            self.head.prev = DoubleNode(key, value)
            self.head.prev.next = self.head
            self.head = self.head.prev
        self.num_elements += 1

    def remove(self, dele_ref):
        if self.head is None or dele_ref is None:
            return

        if dele_ref == self.head:
            self.head = self.head.next
            self.head.prev = None

        elif dele_ref == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            dele_ref.next.prev = dele_ref.prev
            dele_ref.prev.next = dele_ref.next

        self.num_elements -= 1

    def size(self):
        return self.num_elements

    def __repr__(self):
        res = []
        curr = self.head

        while curr is not None:
            res.append(str(curr))
            curr = curr.next

        return " === ".join(res)


if __name__ == '__main__':
    llist = DoublyLinkedLists()

    for i in range(10):
        llist.append(i, i)

    # Expected: Node(0, 0) === Node(1, 1) === Node(2, 2) === Node(3, 3) ===
    # Node(4, 4) === Node(5, 5) === Node(6, 6) === Node(7, 7) === Node(8, 8)
    # === Node(9, 9)
    print(llist)
