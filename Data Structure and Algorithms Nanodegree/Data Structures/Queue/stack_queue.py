import sys

sys.path.append("../Stack/")

from pythonic_stack import Stack


class Queue(Stack):
    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        self.push(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)


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
