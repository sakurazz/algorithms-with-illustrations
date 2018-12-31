
# DFS


![binary search](https://i.imgur.com/RVGtn22.gif)


## Notes

> DFS是点扩展：天生记路径



## key words

- permutation: [46](https://repl.it/@WillWang42/permute)
- detect cycle: [google](https://willwang-x.github.io/2018/02/shift)
- connected component:
- **path** 

## Corner cases


## Q&A

### DFS vs Backtracking

* [Backtracking](https://www.wikiwand.com/en/Backtracking) is a more general purpose algorithm.
* [Depth-First search](https://www.wikiwand.com/en/Depth-first_search) is a specific form of **backtracking** related to searching tree structures. 

> One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch before backtracking.

It uses backtracking as part of its means of working with a tree, but is limited to a tree structure.

Backtracking, though, can be used on any type of structure where portions of the domain can be eliminated - whether or not it is a logical tree. The Wiki example uses a chessboard and a specific problem - you can look at a specific move, and eliminate it, then backtrack to the next possible move, eliminate it, etc.

from [What's the difference between backtracking and depth first search?](https://stackoverflow.com/questions/1294720/whats-the-difference-between-backtracking-and-depth-first-search)

## Exmaple 



## API  


## Thanks 

https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

## 木桩训练 

* [112. Path Sum](https://leetcode.com/problems/path-sum/submissions/1)
* [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
* [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)
* [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)
* [851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/description/)
* subset