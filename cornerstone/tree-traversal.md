# Tree Traversal 

以 Preorder 为例

Typical: 

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)


## Recursive 

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
 
## Iterative
 
 ```python 
 class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        while root or stack:
            if root is None:
                root = stack.pop()
            if root:
                ans.append(root.val)
                stack.append(root.right)
                root = root.left 
        return ans 
 ```
 
## Iterative: Better formula 
 
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

##  Iterative: Code for Human


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

## Morris

```python 
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