# 283. Move Zeroes


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


Example:

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
```

Notes:

1. You must do this in-place without making a copy of the array.
1. Minimize the total number of operations.

## Idea 

1. 如果要in-place, 先找到 `0`的位置`i`, 然后找到 `0` 之后的第一个 `非零`的位置`j`, 然后交换。然后继续找下一个`0`, 和下一个 `非零`，重复以往。
2. 思路2是将`非零`元素，往前顺序交换, 则可。需要两个变量： 1）顺序坐标 2） 非零元素坐标。 快慢指针。

Corner case 

```
[]
[0]
[1]
[0,1]
[1,0]
[0,0,0]
[1,2,3]
[0,0,0,1,2,3]
[1,2,3,0,0,0]
```


## Code 

``` python
# Time: O(2n) where n = len(nums)
# Space: O(1)
# 283. Move Zeroes


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) or j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            while (j < i) or (j < len(nums) and nums[j] == 0):
                j += 1
            if j >= len(nums):
                return 
            if nums[i] != 0:
                return 

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
```

Solution2:

``` python 
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero = 0           
        for i, num in enumerate(nums):
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
            if non_zero >= len(nums):
                return 
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1

```