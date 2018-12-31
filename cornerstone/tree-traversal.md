# Tree Traversal


Typical: 

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)


## Preorder Traversal

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

### 1. Recursive

```python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helper([], root)
    
    def helper(self, ans, root):
        if root is None:
            return ans 
        ans.append(root.val)
        return ans + self.helper([], root.left) + self.helper([], root.right)
```

###  2.1 Iterative: Better formula 

imitate the way built-in recursive code does


``` python 
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans 
```

## 2.2 Iterative: Code for Human

```python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(0, root)]
        ans = []
        while stack:
            opt, node = stack.pop()
            if node is None: 
                continue 
            if opt == 0: 
                stack.append((0, node.right)) # 0: to visit its children
                stack.append((0, node.left))
                stack.append((1, node)) # 1: to print 
            else:
                ans.append(node.val)
        return ans
```

### 3. Morris 

``` python

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        ans = []
        while curr:
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    ans.append(curr.val)
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right
        return ans
```