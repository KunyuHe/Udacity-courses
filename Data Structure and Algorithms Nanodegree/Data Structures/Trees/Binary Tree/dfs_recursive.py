"""
Pre-order
"""
from binary_tree import Tree
from node import Node


def pre_order(tree):
    visit_order = []
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.value)
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    print(pre_order(tree))
