class Stack():
    def __init__(self, init_size=10):
        self.capacity = init_size
        self.arr = [None for _ in range(init_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.size() == self.capacity:
            self.resize()
        self.arr[self.next_index] = value

        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        self.next_index -= 1
        self.num_elements -= 1

        tmp = self.arr[self.next_index]
        self.arr[self.next_index] = None

        return tmp

    def top(self):
        return self.arr[self.next_index-1]

    def resize(self):
        self.capacity *= 2

        tmp = self.arr[:]
        self.arr = [None for _ in range(self.capacity)]

        for idx, num in enumerate(tmp):
            self.arr[idx] = num

        tmp = None

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        if self.is_empty():
            return "<stack is empty>"
        else:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join(
                [str(item) for item in self.arr[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s


if __name__ == '__main__':
    pass
