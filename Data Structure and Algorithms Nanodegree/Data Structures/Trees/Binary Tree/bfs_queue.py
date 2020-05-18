"""
Pre-order traversal
"""

import sys

sys.path.append("../../Queue/")

from array_queue import Queue
from node import Node
from binary_tree import Tree


def bfs(tree):
    queue = Queue()
    visit_order = []
    queue.enqueue(tree.get_root())

    while not queue.is_empty():
        node = queue.dequeue()
        visit_order.append(node.value)

        if node.has_left_child():
            queue.enqueue(node.get_left_child())

        if node.has_right_child():
            queue.enqueue(node.get_right_child())

    return visit_order


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    print(bfs(tree))
