from collections import defaultdict
from typing import Mapping, List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self) -> List[str]:
        suffix_lst = []

        def traverse(children: Mapping[str, TrieNode], suffix: str = ''):
            for char, child in children.items():
                if child.is_word:
                    suffix_lst.append(suffix + char + " ")
                traverse(child.children, suffix + char)

        traverse(self.children)
        return suffix_lst
