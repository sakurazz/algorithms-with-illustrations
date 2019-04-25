# 523. Continuous Subarray Sum

Given a list of **non-negative** numbers and a target **integer** k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an **integer**.

Example 1:

```
Input: [23, 2, 4, 6, 7],  k=6
Output: True
```

Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

```
Input: [23, 2, 6, 4, 7],  k=6
Output: True
```

Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

**Note:**

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

## Idea 

1. 最直接的想法，就是把每一种可能都计算一遍，需要O(n^2), 注意 k = 0的情况。
2. 如何优化呢？那么意味着只**遍历一遍**`nums`, 关键词是 continuous array, 那么我们有没有可能像「sliding window」中头指针`i`和尾指针`j`， 知道什么往前移动`i`呢？
3. 无论如何，所有的subarray，我们都要遍历一遍。那么意味着我们有某种快速**检查**的方法 —— hashmap.

```
            sum(array) / k = 7 ... 1 
     -----**----**
     -----
     sum(subaray) / k = 7 ... 1
```

有用的信息，其实就是**商**和**余数**。我们记录遍历过的所有subaray: 

> {quotient:remainder}

这样就可以往回看，check所有以当前节点**结束**，所有新的subarray有没有符合条件的。

### Corner Case 


```
[]
1
[1, 2]
0
[0]
0
# why we add quo_rem[0] = -1
[23,2,4,6,7]
6
```

## Code 


### Brute Force: O(N^2), O(1)

``` python 
# Time: O(n^2) where n = len(nums)
# Space: O(1) 
# Brute Force 

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False 
        for i, num in enumerate(nums[:len(nums)-1]):
            temp = num
            for j, nxt in enumerate(nums[i+1:]):
                temp += nxt 
                if k == 0:
                    if temp == k:
                        return True 
                else:
                    if temp % k == 0:
                        return True 
        return False 
```

### Hashmap: O(N), O(N)

``` python 
# Time: O(n) where n = len(nums)
# Space: O(n) 

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False 
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i-1] == 0:
                    return True 
            return False 
        
        remainder = {}
        remainder[0] = -1
        sum_subarray = 0 
        for i, num in enumerate(nums):
            sum_subarray += num
            _, rem = divmod(sum_subarray, k)
            if rem in remainder:
                if i - remainder[rem] > 1:
                    return True  
            else:
                remainder[rem] = i
        return False 
```

## 优化：Handle k = 0 

可以把 k = 0 的特殊处理，因为我只关心余数，具体看以下例子：

```
 0  1  2  3  4  5  6
[1, 2, 3, 4, 0, 0, 5], k = 0
 sum(1,2,3,4) = 10  -> remainder[10] = 3
 sum(1,2,3,4,0,0) = 10 -> in remainder 
```

``` python 
# Time: O(n) where n = len(nums)
# Space: O(n) 

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False 
        
        remainder = {}
        remainder[0] = -1
        rem = 0 
        for i, num in enumerate(nums):
            rem += num
            if k != 0: rem = rem % k
            if rem in remainder:
                if i - remainder[rem] > 1:
                    return True  
            else:
                remainder[rem] = i
        return False 
```