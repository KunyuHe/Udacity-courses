class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def get_char(self):
        return self.char

    def get_freq(self):
        return self.freq

    def set_char(self, char):
        self.char = char

    def set_freq(self, freq):
        self.freq = freq

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def is_leaf(self):
        return self.char is not None

    def __gt__(self, other):
        if not isinstance(other, HuffmanNode):
            raise TypeError(f"Cannot compare. {other} is not a HuffmanNode.")
        return self.freq > other.freq

    def __add__(self, other):
        if not isinstance(other, HuffmanNode):
            raise TypeError(f"Cannot add. {other} is not a HuffmanNode.")
        return HuffmanNode(None, self.freq + other.freq)

    def __repr__(self):
        return f"Node({self.char}, {self.freq})"


if __name__ == '__main__':
    pass
