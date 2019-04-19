# Binary tree


> A tree whose elements have at most 2 children.

## 基础知识

 **Recursive algorithms** are well-suited to problems on trees. Remember to include space implicitly allocated on the **function call stack** when doing space complexity analysis. 
 
Some tree problems have simple brute-force solutions that use 0(n) space solution, but subtler solutions that uses the **existing tree nodes** to reduce space complexity to 0( 1). 

Consider **left- and right-skewed trees** when doing complexity analysis. Note that 0(h) complexity, where h is the tree height, translates into 0(log n) complexity for balanced trees, but 0(n) complexity for skewed trees. [Problem 10.12]

If each node has a **parent field**, use it to make your code simpler, and to reduce time and space complexity. [Problem 10.10]

It's easy to make the **mistake** of treating a node that has a single child as a leaf. 

## 典型应用


- 基本**操作**(寻找特定节点)
	- [156 upside down] 	
	- [617 merge]
	- [669 Trim] 
	- [226 invert] 
	- [606 construct] 
	- [108 convert]
	- [107 level order]
	- [114 Flatten BT to Linked List]
	- [426 convert BS to linked list]
	- [654 build maximum](https://leetcode.com/problems/maximum-binary-tree/)
	- [701 insert]
	- [814 pruning](https://leetcode.com/problems/binary-tree-pruning/)
	- [889 construct from preorder & postorder]
	- [951 flip](https://leetcode.com/problems/flip-equivalent-binary-trees/)
	- [971 Flip BT to Preorder]
	- [99 recover]
- **查看**判断(判断树的性质) 
	- [96 unique]	 
	- [965 univalued] 
	- [104 depth]
	- [111 minimum depth](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
	- [124 path sum]
	- [173 iterator]
	- [199 right side view]
	- [366 find leaves]
	- [637 average]
	- [655 print]
	- [662 Maximum width]
	- [563 tilt]
	- [543 diameter]
	- [545 boundary]
	- [257 path]
	- [236 lowest common ancestor]
	- [671 second minimum]
	- [270 cloest value]
	- [110 balanced](https://leetcode.com/problems/balanced-binary-tree/)
	- [742 closest leaf]
	- [894 full](https://leetcode.com/problems/all-possible-full-binary-trees/)
	- [863 K distance]
	- [958 completeness]

* Construct 
* Convert: 树和其他数据结构的相互转换 	
* 树的路径问题

## 最佳实践

- 操作，查看，计算
- search 
- recursively 
- construct 
- convert 
- path 

### recursive (merge)

``` python
def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1: return t2
    if not t2: return t1
    t1.val += t2.val
    t1.left  = self.merge_trees(t1.left, t2.left)
    t1.right = self.merge_trees(t1.right, t2.right)
    return t1
```

### iterative (view)

``` python
def right_side_view(self, root: TreeNode) -> List[int]:
    if not root: return []
    front = [root]
    sight = []
    while front:
        sight.append(front[-1].val)

        nxt = []
        for node in front: 
            if node.left:  nxt.append(node.left)
            if node.right: nxt.append(node.right)
        front = nxt 

    return sight 

```
### pass info to children, `target -= node.val` 

``` python
def max_ancestor_diff(self, node, high, low):
    if not node:
        return high - low
    high = max(high, node.val)
    low  = min(low,  node.val)
    return max(max_ancestor_diff(node.left,  high, low), \
               max_ancestor_diff(node.right, high, low))
```

### get info from children, `sum(path)`

``` python
def min_depth(self, root: TreeNode) -> int:
    if not root: return 0
        
    children = [root.left, root.right]
    if not any(children): return 1

    min_ = float('inf')
    for c in children:
        if c:  min_ = min(min_depth(c), min_)
        
    return min_ + 1
```

### corner case 

- root == `None`
- negative value 
- empty tree\ single node \ two nodes
- Very skewed tree (like a linked list).


## 木桩训练

## Explain

## Q&A

## Thanks

