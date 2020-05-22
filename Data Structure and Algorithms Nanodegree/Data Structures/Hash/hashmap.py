class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None


class HashMap:
    LOAD_FACTOR = 0.7

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31  # or 37
        self.num_entries = 0
        self.capacity = initial_size

    def put(self, key, value):
        """
        Separate chaining with linked list.
        :param key:
        :param value:
        :return:
        """
        idx = self.hash(key)
        new_node = Node(key, value)

        head = self.bucket_array[idx]

        # Check if the key is already in the bucket
        node = head
        while node is not None:
            # Key is unique. Hence update value.
            if node.key == key:
                node.value = value
                return None
            node = node.next

        # Prepend the node to a existing or new bucket linked list
        new_node.next = head
        self.bucket_array[idx] = new_node
        self.num_entries += 1

        # Check load factor
        lf = self.size() / self.capacity
        if lf > self.LOAD_FACTOR:
            self._rehash()

    def get(self, key):
        idx = self.hash(key)
        node = self.bucket_array[idx]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def delete(self, key):
        idx = self.hash(key)
        prev, curr = None, self.bucket_array[idx]

        while curr is not None:
            if key == curr.key:
                if prev is None:
                    self.bucket_array[idx] = curr.next
                else:
                    prev.next = curr.next
                    curr = None
                self.num_entries -= 1
                return None
            prev, curr = curr, curr.next

    def hash(self, key):
        key = str(key)
        p = 1
        hash_code = 0

        # Base p
        for character in key:
            hash_code = (hash_code + ord(character) * p) % self.capacity
            p = (p * self.p) % self.capacity

        return hash_code % self.capacity

    def _rehash(self):
        arr = self.bucket_array
        self.capacity *= 2
        self.num_entries = 0
        self.bucket_array = [None for _ in range(self.capacity)]

        for head in arr:
            while head is not None:
                self.put(head.key, head.value)
                head = head.next

    def size(self):
        return self.num_entries

    def __repr__(self):
        output = ""

        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next

        return output


if __name__ == '__main__':
    # Test the collision resolution technique
    hash_map = HashMap(5)

    hash_map.put("one", 1)
    hash_map.put("two", 2)
    hash_map.put("three", 3)
    hash_map.put("neo", 11)

    print(hash_map)

    hash_map.delete("one")
    print(hash_map)
