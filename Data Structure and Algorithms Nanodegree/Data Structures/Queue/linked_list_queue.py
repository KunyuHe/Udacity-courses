import sys

sys.path.append("../Array and Linked Lists/Linked List/")

from node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None

        val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return val

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print("Pass" if (q.dequeue() == 2) else "Fail")
    print("Pass" if (q.dequeue() == 3) else "Fail")
    print("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print("Pass" if (q.size() == 1) else "Fail")
