import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode('utf-8'))

        return sha.hexdigest()

    def get_data(self):
        return self.data

    def get_hash(self):
        return self.hash

    def __repr__(self):
        return (f"Block: data - {self.data}\n"
                f"time stamp - {self.timestamp}\n"
                f"hash - {self.hash}\n")


if __name__ == '__main__':
    print(Block('my balance: 10 | cash flow: +25 | final balance: 35', None))
