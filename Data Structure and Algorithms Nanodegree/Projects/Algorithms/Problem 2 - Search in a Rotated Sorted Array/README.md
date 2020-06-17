# Problem Statement

You are given a sorted array which is rotated at some random pivot point. Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]. You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

# Solution

Time complexity for the linear search is `O(n)`. It does not exploit the fact that the given array is sorted and just rotated at some random pivot point.

The interesting property of a rotated sorted array is that divided it into two halves, at least one of the two would be be sorted. If the mid point happens to be the pivot, then both halves would be sorted. We can find out which is sorted by comparing their starting and ending elements. If the key is present in the sorted halve, we recursively call binary search on that halve. Else, we recursively call the search routine on the other half.

# Complexity

Time complexity for the algorithm is `O(log(n))` as one of the sub-arrays would always be sorted, and we discard half of the array at each recursive call. Space complexity is `O(1)` as we do not use any data structure whose size depends on input size.