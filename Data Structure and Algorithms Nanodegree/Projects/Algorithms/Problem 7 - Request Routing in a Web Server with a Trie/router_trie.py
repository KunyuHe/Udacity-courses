from typing import Union, List

from node import RouteTrieNode


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, paths: List[str], handler: str):
        curr = self.root

        for path in paths:
            curr = curr.children[path]
        curr.handler = handler

    def find(self, paths: List[str]) -> Union[str, None]:
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root

        for path in paths:
            if path not in curr.children:
                return

            curr = curr.children[path]
        return curr.handler
