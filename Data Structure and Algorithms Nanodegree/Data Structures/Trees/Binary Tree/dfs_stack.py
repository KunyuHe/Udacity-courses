"""
Pre-order traversal
"""

import sys

sys.path.append("../../Stack/")

from array_stack import Stack
from node import Node
from binary_tree import Tree


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
                visited_left: {self.visited_left}
                visited_right: {self.visited_right}
             """
        return s


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()

    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)

    count = 0
    while (node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    pre_order_with_stack(tree, debug_mode=True)
