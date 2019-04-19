# Binary Search Tree

<img src="https://i.imgur.com/oAQtYTl.gif" alt="binary search tree" width="200"/>

## 基础知识

Binary Search Tree is a node-based binary tree data structure which has the following properties:

* The left subtree of a node contains only nodes with keys lesser than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* The left and right subtree each must also be a binary search tree.

## 典型应用

- look up in O(nlogn)

## 最佳实践

- isBST
- inorder generator
- kth smalllest (iterative)


### isBST

``` python
def is_valid_BST(root, lower = float("-inf"), upper = float("inf")):
    if not root: 
    	return True 
    
    if root.val <= lower or root.val >= upper:
        return False 
    
    return  is_valid_BST(root.left,  lower, root.val) and \
            is_valid_BST(root.right, root.val, upper)
```

### inorder generator 

``` python
def inorder(self, root):
    if root:
        for val in self.inorder(root.left):  yield val
        yield root.val
        for val in self.inorder(root.right): yield val
```


### kth smallest (iterative+inorder)

``` python
def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()

        k -= 1
        if k == 0:
            return node.val

        root = node.right 
``` 


## 木桩训练

- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Explain

## Q&A

## More