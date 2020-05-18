import sys

sys.path.append("../Array and Linked Lists/Linked List/")

from node import Node


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        """
        Push to head to avoid traversing the linked list everytime
        :return:
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return val

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print("Pass" if (stack.pop() == 60) else "Fail")
    print("Pass" if (stack.pop() == 40) else "Fail")
    print("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print("Pass" if (stack.size() == 3) else "Fail")
