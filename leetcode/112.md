
# 112. Path Sum


Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


## Idea 

* 1. dfs, sum - root.val 然后变成一个新的子问题。Base 是 sum == 0

## Code 

### 第一版: 原始的思路过程

``` python 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False 
        sum -= root.val
        if root.left is None and root.right is None:
            if sum == 0:
                return True 
            else:
                return False 
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```
### 第二版

``` python 
# Time: O(n)
# Space: O(1)
# Path Sum 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: # Edge case
            return False 
        if root.left is None and root.right is None and root.val == sum:
            return True 
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
```