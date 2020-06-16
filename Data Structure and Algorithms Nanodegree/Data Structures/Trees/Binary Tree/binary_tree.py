import sys

from node import Node

sys.path.append("../../Queue/")

from array_queue import Queue


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        """bfs pre-order"""
        level = 0
        root = self.get_root()
        queue = Queue()
        visit_order = []

        queue.enqueue((root, level))

        while not queue.is_empty():
            node, level = queue.dequeue()

            if node is None:
                visit_order.append(("<empty>", level))
                continue

            visit_order.append((str(node), level))

            if node.has_left_child():
                queue.enqueue((node.get_left_child(), level + 1))
            else:
                queue.enqueue((None, level + 1))

            if node.has_right_child():
                queue.enqueue((node.get_right_child(), level + 1))
            else:
                queue.enqueue((None, level + 1))

        s = "Trie\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    print(tree)
