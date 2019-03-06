# 894. All Possible Full Binary Trees


## Idea

* 问题可以被分解为几个子问题，如F(7) 可以被分解为(左，右) = (1,6),(3,5), (6,1) 解的组合。
* Base case: F(1) = [(ListNode(0)]
* 这样就可以递归的写了，避免重复计算，还可以使用hashmap, 保留计算过的结果

## Code 

```python
# Time: O(2^N) 
# Space: O(2^N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {0: [], 1:[TreeNode(0)]}
    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in self.memo:
            res = []
            for i in range(1,N,2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N-i-1):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        res.append(node)
            self.memo[N] = res
        return self.memo[N] 
        
```