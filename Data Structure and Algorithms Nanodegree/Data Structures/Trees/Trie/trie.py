from node import TrieNode


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        if not word:
            return

        curr = self.root

        for char in word:
            curr = curr.children[char]

        curr.is_word = True


    def exists(self, word):
        """
        Check if word exists in trie
        """
        pass