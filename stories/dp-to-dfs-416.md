# DP to DFS: 416 


This problem is essentially let us to find whether there are several numbers in a set which are able to sum to a specific value (in this problem, the value is sum/2).

- [x] 416
- [ ] [494. Target Sum](https://leetcode.com/problems/target-sum/discuss/97369/Evolve-from-brute-force-to-dp): evolve from brute force to dp



## 1. DP - 0/1 knapsack 

![dp](https://i.imgur.com/e0vRxsp.png)


``` python 
# Time: O(n * half) where n = len(nums), half = sum(nums) / 2
# Space: O(half)
# 416. Partition Equal Subset Sum

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        quotient, remainder =  divmod(sum(nums), 2)
        if remainder == 1: return False 
        
        dp = [True] + [False for _ in range(quotient)]
        
        for i in range(len(nums)):
            for j in range(quotient, nums[i]-1, -1):
                dp[j] = dp[j-nums[i]] | dp[j]
        return dp[-1]
```

## DFS 

Target minus each element as `Target` for next recursion of the rest elements.

**Base case:**

* Target < 0 (ignore)
* Target == 0 (return True)

Recursive case: Otherwise

![DFS](https://i.imgur.com/TRocZQ3.png)

``` python 
# 416. Partition Equal Subset Sum

class Solution(object):
    def canPartition(self, nums):        
        
        def helper(start, target):         
            if target < 0:  return
            if target == 0: return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]): return True
            return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2) 
```


## DFS with memoization 

![](https://i.imgur.com/vsbdCxu.png)

```python 
# Time: O(n * t) where n = len(nums) and t is the number of targets  
# Space: O(len(cache))
# 416. Partition Equal Subset Sum
'''
Why better than DP? Cause we only cache what we need (valid states) instead of all continuous states . 
'''

class Solution(object):
    def canPartition(self, nums):
        cache = {}
        
        def helper(start, target):         
            if target in cache:
                return cache[target]
            if target < 0:  return 
            if target == 0: return True
            
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            cache[target] = False
            return False
        
        return False if sum(nums)%2 else helper(0, sum(nums)/2)
```


## Thanks

* [494: evolve from brute force to dp](https://leetcode.com/problems/target-sum/discuss/97369/Evolve-from-brute-force-to-dp)