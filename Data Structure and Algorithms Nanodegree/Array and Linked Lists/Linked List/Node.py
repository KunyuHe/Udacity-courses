class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class DoubleNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.previous = None


if __name__ == '__main__':
    pass
