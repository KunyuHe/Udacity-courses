# Problem Statement

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

**Bonus Challenge:** Is it possible to find the max and min in a single traversal?

# Solution

The solution is fairly straightforward. We can initialize the running minimum as `np.Inf`, and the running maximum as `-np.Inf`. Then we would traverse the given array once and update the running minimum/maximum if the current element is smaller/larger. By this we can find the global max and min in a single traversal. 

# Complexity

As the proposed algorithm traverses the elements in the input array once, its time complexity is `O(n)` as desired. The space complexity is `O(1)` as we do not employ any data structure whose size depends on the input size.