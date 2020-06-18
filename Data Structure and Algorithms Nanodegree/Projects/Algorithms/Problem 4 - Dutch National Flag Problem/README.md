# Problem Statement

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

**Note:** `O(n)` does not necessarily mean single-traversal. For example, if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

# Solution

To sort the input array that consists of only 0, 1, and 2 in a single traversal, we can use a hash map mapping digits to their frequency. We traverse the list once, and count the number of digits. Then we initial an empty result list, loop through the hash map of fixed length 3, and extend the result list by `[digit]*frequency`.

# Complexity

Since we only traverse the input list once, time complexity of the proposed algorithm is `O(n)`. In terms of space complexity, the frequency map is of fixed length 3, hence independent from the input size. However, we use a result list to host the sorted array. Space complexity is `O(n)`.