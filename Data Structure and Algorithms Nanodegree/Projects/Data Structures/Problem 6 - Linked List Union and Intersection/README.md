# Problem Statement

The task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

The functions will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

# Design

For this problem, we can make use of the `set()` data structure. It offers `union()` and `intersection()` methods that suits our needs well. Before that, we can first transform the linked lists into a data structure easier to work with, for example, a list in `O(n)`. Then we can do the set operations, and push the values back into a merged linked lists.

*Time complexity* for union is `O(n)` as we just need to add two lists together, construct the set, and create a new linked list. For intersection, the time is bounded by and linear in the size of the smaller set. Hence, it is `O(n)`.

*Space complexity* is also quite straightforward as we created a new linked lists with size proportional to input size. It is `O(n)` for both union and intersection.