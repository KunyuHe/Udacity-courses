from binary_tree import Tree
from node import Node


class BST(Tree):
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    @staticmethod
    def compare(self, other):
        if self.get_value() == other.get_value():
            return 0
        return [-1, 1][int(self.get_value() < other.get_value())]

    def insert(self, value):
        if self.get_root() is None:
            self.set_root(value)
            return None

        def _insert(node, new_node):
            comparison = self.compare(node, new_node)

            if comparison == 0:
                node.set_value(new_node.get_value())

            elif comparison == -1:
                if node.has_left_child():
                    _insert(node.get_left_child(), new_node)
                else:
                    node.set_left_child(new_node)

            else:
                if node.has_right_child():
                    _insert(node.get_right_child(), new_node)
                else:
                    node.set_right_child(new_node)

        _insert(self.get_root(), Node(value))

    def search(self, value):
        root = self.get_root()
        if root is None:
            return False

        search_node = Node(value)

        def _search(node):
            comparison = self.compare(node, search_node)
            if comparison == 0:
                return True

            if comparison == -1:
                if node.has_left_child():
                    return _search(node.get_left_child())
                else:
                    return False

            if comparison == 1:
                if node.has_right_child():
                    return _search(node.get_right_child())
                else:
                    return False

        return _search(root)

    @staticmethod
    def find_next_higher(node):
        curr = node

        while curr.left is not None:
            curr = curr.left

        return curr

    def diameter(self):
        """
        Diameter of a Binary Tree is the maximum distance between any two nodes.
        :return: diameter
        """
        root = self.get_root()

        def _diameter(node):
            if node is None:
                return 0, 0

            l_height, l_diameter = _diameter(node.get_left_child())
            r_height, r_diameter = _diameter(node.get_right_child())

            height = max(l_height, r_height) + 1

            return height, max(l_diameter, r_diameter, l_height + r_height)

        return _diameter(root)[1]

    def path_to_root(self, value):
        path_node = Node(value)

        def _path(node):
            if node is None:
                return None

            if node.get_value() == value:
                return [path_node]

            l = _path(node.get_left_child())
            if l is not None:
                l.append(node)
                return l

            r = _path(node.get_right_child())
            if r is not None:
                r.append(node)
                return r

            return None

        path = _path(self.get_root())
        if path is None:
            return None

        return path[::-1]


if __name__ == '__main__':
    tree = BST()
    tree.insert(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(2)
    tree.insert(5)
    print(tree)
    print(tree.diameter())
    print(tree.path_to_root(2))

    print(f"""
    search for 8: {tree.search(8)}
    search for 2: {tree.search(2)}
    """)
