# Problem Statement

The goal will be to design a data structure known as a **Least Recently Used (LRU) cache**. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both `get` and `set` operations as an `use operation`.

Your job is to use an appropriate data structure(s) to implement the cache.

- In case of a `cache hit`, your `get()` operation should return the appropriate value.
- In case of a `cache miss`, your `get()` should return -1.
- While putting an element in the cache, your `put()` / `set()` operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take `O(1)` time.

# Design

The problem requires our cache implementation to not only store the values, but also track the relative order of the user operations in order to figure out which entry to remove as the least recently used entry when our cache reaches its capacity.

The data structure we used to implement the cache is a linked list. We can track the order by prepending the most recently used entry to the head and remove the least recently used entry at the tail when the cache memory reaches its limit. When a user operation happens to any nodes except for the head node, we can mark it as the most recently used entry by removing it and prepending it to our linked list.

However, a linked list alone cannot guarantee a constant run time. The `get()` operation would have to traverse the cache to check if the key is present in the cache and get the corresponding value. Meanwhile, when we update the relative order to reflect user operations, we would also have to traverse the linked list to remove the node and prepend it. If the capacity or our cache is proportion to input size, the run time for both `get()` and `set()` will be O(n).

To optimize, we can use a hash map to map the key to a pointer to the node that stores the value. By doing so, we will be able to know whether a key is present in the cache, retrieve its value, and update the cache to reflect change in relative order or user operations in constant time. To facilitate updating the order and removing the tail node, we use a doubly linked list as our cache. Each node stores both key and value so that we can easily remove the least recently used pair from the hash map. We would use a python dictionary to map search keys to the nodes in the cache so that we can access the nodes and change their relative ordering in `O(1)`. It is the case because we could learn whether the key is present in the cache by checking the hash map, and we could modify the cash through the pointer to avoid traversing the linked list. See below for the file structures.

Programming defensively, we need to watch for degenerate cases when the search key is `None`, or when the search key is not hashable, for example, a list.

A cleaner implementation in Python is using `OrderedDict` to serve as the cache where the key, value pairs are ordered relatively. However, in the spirit of practicing the use of the general data structures, we choose not to do so.

# Files

- .[LRU_Cache.py](LRU_Cache.py): contains the `LRU_Cache` class as an implementation of the LRU cache with `get()` and `set()` methods that run in O(1) time.
- [doubly_linked_lists.py](doubly_linked_lists.py): contains the `DoublyLinkedLists` class that servers as the data structure to store key, value pairs and tracks the relative order of usage.
- [node.py](node.py): contains the `DoubleNode` class that serves as the basic element of the doubly linked lists cache and stores both key and value.
- [test.py](test.py): contains test cases for the LRU cache implementation.







