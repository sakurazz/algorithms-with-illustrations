# 46. Permutations



Given a collection of distinct integers, return all possible permutations.

Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# Idea 

* 想法很直接，DFS

# Code 

## Wrong code: deep copy & shallow copy 

``` python 
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(temp, visited, nums):
            if len(temp) == len(nums):
                self.res.append(temp)  # change to temp[:] 传值而非引用
                
            for num in nums:
                if num not in visited:
                    temp.append(num)
                    visited.add(num)
                    dfs(temp, visited, nums)
                    visited.remove(num)
                    temp.pop()
        
        dfs([], set(), nums)
        
        return self.res 

```

## Right code 


``` python 
# Time: O(n!)
# Space: O(n) where n == len(nums)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(temp, visited, nums):
            if len(temp) == len(nums):
                self.res.append(temp[:])
                
            for num in nums:
                if num not in visited:
                    temp.append(num)
                    visited.add(num)
                    dfs(temp, visited, nums)
                    visited.remove(num)
                    temp.pop()
        
        dfs([], set(), nums)
        
        return self.res 

```

## BFS solution 

``` python 
'''
e.g.
n = [1,2,3]
perms = [[]]
[1],0
[[1]]
[[1,2],[2,1]]
[[3,1,2],[1,3,2],[1,2,3],[3,2,1],[2,3,1],[2,1,3]]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        # We are going to insert a new element to every position in a old permutaion in every object in the list.
        perms = [[]]
        for n in nums:
            new_perms = []
            
            for perm in perms:
                for i in xrange(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            
            perms = new_perms
        return perms
```

## variant: parity permutation

给你一个整数n, 要求返回List<List<Integer>>, 每个List<Integer> 都由1到n组成并且奇偶相间, 按照"lexicographic order"排好。

```
n = 4. you should return:
[[1,2,3,4],
[1,4,3,2],
[2,1,4,3],
[2,3,4,1],
[3,2,1,4],
[3,4,1,2],
[4,1,2,3],
[4,3,2,1]]
```

``` python 
# parity permutation LC 46 DFS 

def permute(num):
    """
    :type nums: int 
    :rtype: List[List[int]]
    """  
    nums = [i+1 for i in range(num)]  
    res = []
    
    def dfs(nums, temp, temp_set):
        if len(temp) == len(nums):
            res.append(temp[:])

        for i in range(len(nums)):
            if nums[i] in temp_set:
                continue
            if len(temp) > 0 and (temp[-1] % 2 + nums[i] % 2) != 1:
                continue 
            temp.append(nums[i])
            temp_set.add(nums[i])
            dfs(nums, temp, temp_set)
            temp.pop()
            temp_set.remove(nums[i])
            
    dfs(nums, [], set())
    return res
    
print(permute(4))
```