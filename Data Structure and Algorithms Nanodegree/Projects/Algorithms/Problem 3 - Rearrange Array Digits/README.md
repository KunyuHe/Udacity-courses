# Problem Statement

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

For [1, 2, 3, 4, 5], the expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

# Solution

To obtain the maximum sum, we can first sort the given array and partition it as a generator that one digit goes to the first number and the next digit goes to the second. This would run in `O(nlog(n))` if we implement an algorithm that works like merge sort.

However, we can exploit the fact that each element in the given array is a digit in the range of [0, 9]. Therefore, we can first construct a hash map mapping the digits in descending order to its frequency by traversing the given array. We can then loop through the frequency list of fixed length 10 and assign the digits in the manner described above.

For edge cases where there are less than 2 digits in the given array, the algorithm returns `None`.

# Complexity

Since we only traverse each digit twice (once when we construct the frequency list and another time when we assign the digits), time complexity of the proposed algorithm is `O(n)`. In terms of space complexity, the frequency map is of fixed length 10, hence independent from the input size. Space complexity is `O(1)`.