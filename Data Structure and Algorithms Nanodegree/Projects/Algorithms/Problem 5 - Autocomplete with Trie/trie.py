from typing import Union

from node import TrieNode


class Trie(object):
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word: str):
        # Add a word to the Trie
        curr = self.root

        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def find(self, prefix: str) -> Union[TrieNode, None]:
        # Find the Trie node that represents this prefix
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return
            curr = curr.children[char]

        return curr

    def suffixes(self, prefix: str):
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be string.")

        if not prefix:
            raise ValueError("Prefix cannot be an empty string.")

        node = self.find(prefix)
        if not node:
            return

        suffix_lst = node.suffixes()
        return [suffix.strip(" ") for suffix in suffix_lst]
