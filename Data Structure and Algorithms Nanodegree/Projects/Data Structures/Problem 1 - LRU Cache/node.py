class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_key(self):
        return self.key

    def __repr__(self):
        return f"Node({self.key}, {self.value})"


if __name__ == '__main__':
    pass
