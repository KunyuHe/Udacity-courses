from singly_linked_list import LinkedList


class NestedLinkedList(LinkedList):
    @staticmethod
    def merge(self, other):
        merged = LinkedList()
        if self is None:
            return other
        if other is None:
            return self

        curr1 = self.head
        curr2 = other.head
        while self.head is not None or other.head is not None:
            if curr1 is None:
                merged.append(curr2)
                curr2 = curr2.next
            elif curr2 is None:
                merged.append(curr1)
                curr1 = curr1.next
            elif curr1.value <= curr2.value:
                merged.append(curr1)
                curr1 = curr1.next
            else:
                merged.append(curr2)
                curr2 = curr2.next

        return merged

    def _flatten(self, node):
        if node.next is None:
            return self.merge(node.value, None)

        return self.merge(node.vallue, self._flatten(node.next))

    def flatten(self):
        return self._flatten(self.head)
