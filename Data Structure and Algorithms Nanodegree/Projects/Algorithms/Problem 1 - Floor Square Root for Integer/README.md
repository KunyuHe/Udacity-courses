# Problem Statement

Find the square root of the integer without using any Python library. You have to find the floor value of the square root. For example if the given number is 16, then the answer would be 4. If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`.

# Solution

The idea is to implement an algorithm that works like binary search. Instead of counting with an already sorted array, we use the natural consecution as our imaginary sorted array.

We initialize the start point at 0 and the end point at the given number divided by 2, since floored square root of a natural number (starting from 2) is either half or less. At each iteration, we divide the space into two parts and check if the square of the mid point is larger or smaller than, or equal to the given number. If it's equal to the given number, we break the loop and return the mid point as the desired output. Otherwise, we continue and look into the lower half if the square of the mid point is larger than the given number, and the upper half if the square of the mid point is smaller than the given number. If the loop terminates, we should return the latest mid point. 

# Complexity

Time complexity of the proposed algorithm is  `O(log(n))` since we applied binary search on the consecutive integer array ranging from 0 to `(n // 2)`. The space complexity should be `O(1)` as we do not create any data structure whose size depends on the input size.