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
- delete a node in BST? 


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

### smallest node 

``` python
# smallest node in a sub BST
def _smallest(self, node):
    while node.left:
        node = node.left 
    return node.val
```


### delete the node 

``` python
def delete_node(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return root
    
    if root.val == key:
        if not root.left:  return root.right
        if not root.right: return root.left
        root.val   = self._smallest(root.right)
        root.right = self.deleteNode(root.right, root.val)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)
    else:
        root.left  = self.deleteNode(root.left, key)
        
    return root 
```

## 木桩训练

- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Explain

## Q&A

### 1. Advantages of BST over Hash Table?

Hash Table supports following operations in Θ(1) time.
1) Search
2) Insert
3) Delete

The time complexity of above operations in a self-balancing Binary Search Tree (BST) (like Red-Black Tree, AVL Tree, Splay Tree, etc) is O(Logn).

So Hash Table seems to beating BST in all common operations. When should we prefer BST over Hash Tables, what are advantages. 

Following are some important points in favor of BSTs.

* We can get all keys in **sorted order** by just doing Inorder Traversal of BST. This is not a natural operation in Hash Tables and requires extra efforts.
* Doing order **statistics, finding closest lower and greater elements, doing range queries** are easy to do with BSTs. Like sorting, these operations are not a natural operation with Hash Tables.
* BSTs are **easy to implement** compared to hashing, we can easily implement our own customized BST. To implement Hashing, we generally rely on libraries provided by programming languages.
* With **Self-Balancing BSTs, all operations are guaranteed to work in O(Logn) time.** But with Hashing, Θ(1) is average time and some particular operations may be costly, especially when **table resizing** happens.


## More

- [Advantages of BST over Hash Table](https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/)