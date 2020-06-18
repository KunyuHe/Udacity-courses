from collections import defaultdict
from typing import Union


class RouteTrieNode:
    def __init__(self, handler: Union[str, None] = None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler
