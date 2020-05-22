from block import Block


class BlockChain:
    def __init__(self):
        self.tail = None
        self.num_elements = 0

    def append(self, data):
        if self.tail is None:
            self.tail = Block(data, previous_hash=None)
        else:
            self.tail = Block(data, previous_hash=self.tail)
        self.num_elements += 1

    def search(self, data):
        for node in self:
            if data == node.get_data():
                return node

        return

    def size(self):
        return self.num_elements

    def __iter__(self):
        curr = self.tail
        while curr is not None:
            yield curr
            curr = curr.previous_hash

    def __repr__(self):
        return "\n\t\t|\n\t\t|\n\t\t|\n\t\tV\n\n".join([str(node)
                                                        for node in self][::-1])


def create_mad_men_blockchain():
    madmen = BlockChain()

    for female in ['Betty', 'Midge', 'Rachael', 'Bobbie', 'Suzanne', 'Faye',
                   'Megan']:
        madmen.append(female)

    return madmen


if __name__ == '__main__':
    madmen = create_mad_men_blockchain()

    print(madmen)
