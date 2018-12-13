# 268. Missing Number

> 这道题主要考察你知识的广度，能想到多少方法解决它？

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```


## Show me the code 

``` python 
# Time: O(n)
# Space: O(n)
'''
1. Array
Time: O(n) | Space: O(n)
2. Algorithm: Sort + BinarySearch
Time: O(nlogn) + O(logn) | Space: O(n)
3. Sum: Math 
Time: O(n) | Space: O(1)
4. BitManipulation: XOR 
Time: O(n) | Space: O(1)
5. Data Structure: HashSet
Time: O(n) | Space: O(n)
6. BitSet #Q 
Time: O(n) | Space: O(?)
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        nums_set = set(nums)
        for i in range(n+1):
            if i not in nums_set:
                return i
        
```