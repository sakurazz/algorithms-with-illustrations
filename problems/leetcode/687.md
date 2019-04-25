# 687. Longest Univalue Path


Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

	2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

	2

**Note**: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.



## Idea 

* 三种情况讨论，左边，右边，左边+右边

### Case

```
[5,4,5,1,1,5]
[]
[1]
```

## Code 

### 1.

```python
# Time: O(n) where n = the number of nodes
# Space: O(1)
# 687. Longest Univalue Path


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.helper(root)[1] - 1
    
    def helper(self, root):
        if root is None:
            return 0, 0
        
        left_in, left_max = self.helper(root.left)
        right_in, right_max =self.helper(root.right)
        
        res = max(left_max, right_max, 1)
        root_in = 1
        
        if root.left and root.val == root.left.val:
            root_in = max(root_in, left_in + 1)
        if root.right and root.val == root.right.val:
            root_in = max(root_in, right_in + 1)
        if root.left and root.right and root.val == root.left.val == root.right.val:
            res = max(res, left_in + right_in + 1)
        res = max(res, root_in)
        return root_in, res 
```

### 2. 维持全局最优解

* 这样就少了一个变量，local_max, gobal_max
* 数线，而不是点

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 
        
        def helper(node):
            if node is None:
                return 0
            
            left_in = helper(node.left)
            right_in = helper(node.right)

            node2left, node2right = 0, 0
            if node.left and node.left.val == node.val:
                node2left = left_in + 1
            if node.right and node.right.val == node.val:
                node2right = right_in + 1
            self.res = max(self.res, node2left + node2right)
            return max(node2left, node2right)
        
        helper(root)
        return self.res 
```
