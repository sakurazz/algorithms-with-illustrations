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

- inorder traversal
- isBST

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

## 木桩训练

## Explain

## Q&A

## More