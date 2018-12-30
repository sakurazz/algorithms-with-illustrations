# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Follow up:

If you have figured out the O(n) solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Idea



## Code 

### 1. DP O(n)

```python 
# Time: O(n) where n = len(nums)
# Space: O(1)
# 53. Maximum Subarray
"""

"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        if max(nums) <= 0:
            return res 
        
        local_res = 0
        for i, num in enumerate(nums):
            local_res += num 
            res = max(local_res, res)
            if local_res < 0:
                local_res = 0
        return res 
        
```

### 2. Divide and conquer O(nlogn)

```python
# Time: O(nlogn) where n = len(nums)
# Space: O(1)
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) <= 0:
            return max(nums)
        
        left, right = 0, len(nums)-1
        
        return self.divide_and_conquer(nums, left, right)
    
    def divide_and_conquer(self, nums, left, right):
        # base case 
        if left == right:
            return max(0, nums[left])

        center = (left + right) // 2
        left_max = self.divide_and_conquer(nums, left, center)
        right_max = self.divide_and_conquer(nums, center+1, right)
        
        def max_boarder(start, stop, step):
            sum_so_far = 0
            boarder_max = 0
            for i in range(start, stop, step):
                sum_so_far += nums[i]
                boarder_max = max(boarder_max, sum_so_far)
            return boarder_max 
        
        left_boarder_max = max_boarder(center, left-1, -1)
        right_boarder_max = max_boarder(center+1, right+1, 1)
        
        return max(left_max, right_max, left_boarder_max + right_boarder_max)
        
``` 
