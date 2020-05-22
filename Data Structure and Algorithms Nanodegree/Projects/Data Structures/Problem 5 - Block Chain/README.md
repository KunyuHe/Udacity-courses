# Problem Statement

A [Blockchain](https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use our knowledge of linked lists and hashing to create a blockchain implementation.

[![img](https://video.udacity-data.com/topher/2019/April/5ca8bd1d_untitled-diagram/untitled-diagram.png)](https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/a5f68248-862f-4a72-8682-24b86e2f6d61/lessons/a640374a-90af-40ad-85ff-1c6ce3948219/concepts/24216d22-1e4d-48f5-b224-9191fd5e5941#)

We can break the blockchain down into three main parts.

First is the information hash:

```python
import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
```

We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:

```
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
```

Above is an example of attributes you could find in a `Block` class.

Finally we need to link all of this together in a block chain, which we will be doing by implementing it in a linked list. All of this will help us build up to a simple but full blockchain implementation!

# Design

It's clear that we will use linked list as an implementation of block chain. Since each block can have a pointer pointing to its previous one's hash, we need to track the tail of the linked list. In this case, we would append new blocks to the tail. This runs in `O(1)`. For the `search()` method, we would have to traverse each block once to check whether the block exists and it runs in `O(n)`. Overall, *time complexity* of the block chain implementation is `O(n)`. It's *space complexity* is `O(n)`, linearly dependent on the input size.

# Files

- [blockchain.py](blockchain.py): hosts the `BlockChain()` class, a linked lists implementation of blockchain with `append()`, `search()` and `size()` methods.

- [block.py](block.py): contains the `Block()` class from skeleton as a building block of blockchain. Hosts data, hash, time stamp, and a pointer to the previous hash.

- [test.py](test.py): contains test cases for the blockchain implementation.

  