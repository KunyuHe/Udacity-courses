import heapq
import sys
from collections import Counter

from node import HuffmanNode


class HuffmanTree:
    def __init__(self):
        self.heap = []
        self.char_code = {}

    def grow(self, text):
        char_freq = Counter(text)

        for key, val in char_freq.items():
            node = HuffmanNode(key, val)
            heapq.heappush(self.heap, node)

        # Edge case, only one unique character in the text
        if len(self.heap) == 1:
            node = heapq.heappop(self.heap)

            new_node = HuffmanNode(None, node)
            new_node.set_left_child(node)

            heapq.heappush(self.heap, new_node)

        else:
            while len(self.heap) > 1:
                node1 = heapq.heappop(self.heap)
                node2 = heapq.heappop(self.heap)

                node = node1 + node2
                node.set_left_child(node1)
                node.set_right_child(node2)

                heapq.heappush(self.heap, node)

        return self

    def get_root(self):
        return self.heap[0]

    def encode(self):
        try:
            root = self.get_root()
        except:
            raise ValueError("Nothing in the Huffman Trie.")

        def _encode(node, code):
            if node is None:
                return

            # Leaf node
            if node.is_leaf():
                self.char_code[node.get_char()] = code

            _encode(node.get_left_child(), code + "0")
            _encode(node.get_right_child(), code + "1")

        _encode(root, "")

    def get_mapping(self):
        return self.char_code


if __name__ == '__main__':
    pass
