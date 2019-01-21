# 26. Remove Duplicates from Sorted Array




## Idea 

- Use a `last` index to mark the last position num `A` of the subarray, update its next when `iterate` index points the num `B` is not same as `A`.

### Edge case 

```
[1,1,2]
[0,0,1,1,1,2,2,3,3,4]
[1,2]
[1]
[]
```

## Code 

``` python 
# Time:  O(n) where n = len(nums)
# Space: O(1)
# 26. Remove Duplicates from Sorted Array

"""
   i 
[0,0,1,1,1,2,2,3,3,4]
     j

         i 
[0,1,2,3,4,2,2,3,3,4]
                   j

when not same, update next element 
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0 
        
        if len(nums) == 0:
            return last 
        
        for i, num in enumerate(nums):
            if num != nums[last]:
                nums[last + 1] = num
                last += 1
            
        return last + 1

```