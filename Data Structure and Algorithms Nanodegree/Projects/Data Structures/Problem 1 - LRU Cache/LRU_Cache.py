import collections

import pytest
from doubly_linked_lists import DoublyLinkedLists


class LRU_Cache(object):

    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError((f"Cache capacity is of type {type(capacity)}. "
                             f"It must be an integer."))
        if capacity <= 0:
            raise ValueError("Cache capacity must be a positive integer.")

        self.capacity = capacity
        # Doubly linked list, head is the most recently used, tail is the least
        self.cache = DoublyLinkedLists()
        # Hash map mapping search key to pointers to nodes in the cache
        self.key_node = {}

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent.
        """
        if key is None:
            raise KeyError('Search key is missing.')

        if key in self.key_node:
            node = self.key_node[key]
            value = node.get_value()

            # Update the cache and mapping
            self.cache.remove(node)
            self.cache.prepend(key, value)
            self.key_node[key] = self.cache.head

            return value

        return -1

    def set(self, key, value):
        if key is None:
            raise ValueError('Set key is missing.')
        if not isinstance(key, collections.Hashable):
            raise TypeError(f'Key is of type {type(key)}. It is not hashable.')

        if key in self.key_node:
            # Update the value in the cache
            node = self.key_node[key]
            node.set_value(value)

            self.cache.remove(node)
        else:
            if self.cache.size() >= self.capacity:
                old_key = self.cache.tail.get_key()
                self.cache.remove(self.cache.tail)
                self.key_node.pop(old_key)

        self.cache.prepend(key, value)
        self.key_node[key] = self.cache.head


if __name__ == '__main__':
    # Please refer to module test.py for test cases
    pytest.main()
