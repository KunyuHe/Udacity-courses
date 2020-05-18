class Queue:

    def __init__(self, initial_size=10):
        self.capacity = initial_size
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        # To show there's nothing in the queue yet
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % self.capacity
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            # Reset
            self.front_index = -1
            self.next_index = 0
            return None

        val = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % self.capacity
        self.queue_size -= 1

        return val

    def size(self):
        return self.queue_size

    def resize(self):
        arr = self.arr
        self.capacity *= 2
        self.arr = [None for _ in range(self.capacity)]

        next_idx = 0
        for i in range(self.front_index, len(arr)):
            self.arr[next_idx] = arr[i]
            next_idx += 1

        # When the front index is past 0
        for i in range(0, self.front_index):
            self.arr[next_idx] = arr[i]
            next_idx += 1

        self.front_index = 0
        self.next_index = next_idx

    def is_empty(self):
        return self.size() == 0

    def front(self):
        return self.arr[self.front_index]


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
