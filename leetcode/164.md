# 164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```

Example 2:

```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

## Idea 

* 简单方式就是O(nlogn)
* 更快的方法就是 让 radix sort or bucket sort

## Code

### nlogn 

``` python
# Time: O(nlogn) where n = len(nums)
# Space: O(1)
# 164. Maximum Gap

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        nums.sort()
        
        diff = 0 
        pre = nums[0]
        for i, num in enumerate(nums[1:]):
            diff = max(diff, num - pre)
            pre = num
            
        return diff
```


### Couting sort: Time Limit Exceeded

Last executed input:   [2,99999999]

``` python 

# Time: O(m) where m = max(nums)
# Space: O(m) 
# 164. Maximum Gap

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        buckets = [0 for _ in range(max(nums)+1)]
        
        for _, num in enumerate(nums):
            buckets[num] += 1
            
        diff = 0 
        prev = None 
        for i, bucket in enumerate(buckets):
            if bucket > 0: 
                if  prev != None:
                    diff = max(diff, i - prev)
                prev = i 
                
        return diff
```

### Bucket sort: O(n)


```python
# Time: O(n * klogk) where n = len(nums), k ~= 1
# Space: O(n*k)
# 164. Maximum Gap

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        baseline = min(nums)
        min2max = (max(nums) - baseline) + 1
        size = min2max // len(nums) + 1
        buckets = [[] for _ in range(len(nums))]
        
        for _, num in enumerate(nums):
            which = (num - baseline) // size
            buckets[which].append(num)
                
        def get_max_gap(bucket, diff):
            if len(bucket) <= 1 or diff > size:
                return diff 
            bucket.sort()
            pre = bucket[0]
            for _, num in enumerate(bucket[1:]):
                diff = max(diff, num - pre)
                pre = num
            return diff
        
        diff = 0
        prev = None 
        for _, bucket in enumerate(buckets):
            diff = get_max_gap(bucket, diff)
            if bucket:
                if prev != None:
                    diff = max(diff, min(bucket) - prev)
                prev = max(bucket)
        return diff
```

