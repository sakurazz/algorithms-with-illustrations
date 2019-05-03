
# DFS

<center>
<img src="https://i.imgur.com/RVGtn22.gif" alt="DFS" width="200"/> 
</center>


## 基础知识

> DFS是点扩展：天生记路径

* DFS visit nodes of graph depth wise. It visits nodes until reach a leaf or a node which doesn’t have non-visited nodes.
* Exploration of a node is suspended as soon as another unexplored is found.
* Uses **Stack** data structure to store Un-explored nodes.
* DFS is faster and require **less memory**.
* DFS for binary tree = Preorder traversal

Some Applications:

* **Topological** Sorting.
* Finding **connected** components.
* Solving puzzles such as **maze**.
* Finding **strongly** connected components.
* Finding articulation points (cut vertices) of the graph.

## 典型应用
- **path**: 112, 1022
	- detect cycle: [google](https://willwang-x.github.io/2018/02/shift)
	- topology sort
	- permutation: [46](https://repl.it/@WillWang42/permute)
- connected component: 924, 928
 

## 最佳实践

- Graph 
- Connected component 
	- Iterative 
	- Recursive
- Paths
	- Iterative
	- Recursive
- [Count Connected component](https://repl.it/@WillWang42/dfs-best-practice)

**Graph**

``` python 
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
```

### Connected Component


**Iterative**

```python 
def dfs(graph, start):
    seen, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in seen:
            seen.add(vertex)
            stack.extend(graph[vertex] - seen)
    return seen

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
```

**Recursive**

```python
def dfs(graph, start, seen=set()):
    seen.add(start)
    for nxt in graph[start] - seen:
        dfs(graph, nxt, seen)
    return seen

dfs(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}
```

### Paths 


**Iterative**

```python
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
```

**Recursive**

``` python
def dfs_paths(graph, start, goal, path=None):
	# edge case 
    if path is None:
        path = [start]
	# base case     
    if start == goal:
        yield path
    # general case
    for nxt in graph[start] - set(path):
        yield from dfs_paths(graph, nxt, goal, path + [nxt])

list(dfs_paths(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
```

## 木桩训练 

* [112. Path Sum](https://leetcode.com/problems/path-sum/submissions/1)
* [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
* [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)
* [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)
* [851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/description/)
* subset
* [1034. Coloring A Border](https://leetcode.com/problems/coloring-a-border/): conditional DFS


## Q&A

### 1. DFS vs Backtracking

* [Backtracking](https://www.wikiwand.com/en/Backtracking) is a more general purpose algorithm.
* [Depth-First search](https://www.wikiwand.com/en/Depth-first_search) is a specific form of **backtracking** related to searching tree structures. 

> One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch before backtracking.

It uses backtracking as part of its means of working with a tree, but is limited to a tree structure.

Backtracking, though, can be used on any type of structure where portions of the domain can be eliminated - whether or not it is a logical tree. The Wiki example uses a chessboard and a specific problem - you can look at a specific move, and eliminate it, then backtrack to the next possible move, eliminate it, etc.

from [What's the difference between backtracking and depth first search?](https://stackoverflow.com/questions/1294720/whats-the-difference-between-backtracking-and-depth-first-search)


### 2. DFS vs BFS for Binary Tree

source: [geeksforgeeks](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)

* Breadth First Traversal (Or Level Order Traversal)
* Depth First Traversals
	* Inorder Traversal (Left-Root-Right)
	* Preorder Traversal (Root-Left-Right)
	* Postorder Traversal (Left-Right-Root)

All four traversals require **O(n) time** as they visit every node exactly once. There is difference in terms of **extra space** required.

It is evident that extra space required for Level order traversal is likely to be more when tree is **more balanced** and extra space for Depth First Traversal is likely to be more when tree is **less balanced**.


How to Pick one?

* **Extra Space** can be one factor (Explained above)
	* If the tree is very **deep** and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.
	* If the tree is very **wide**, a BFS might need too much memory, so it might be completely impractical.
	* If solutions are **frequent** but located **deep** in the tree, BFS could be impractical.
	* If the search tree is very **deep** you will need to **restrict** the search depth for depth first search (DFS), anyway (for example with **iterative deepening**).
* Depth First Traversals are typically **recursive** and recursive code requires **function call overheads**.
* The most important points is, BFS starts visiting **nodes** from root while DFS starts visiting nodes from **leaves**. So if our problem is to search something that is more likely to closer to **root**, we would prefer **BFS**. And if the target node is close to a **leaf**, we would prefer **DFS**.


## Thanks 

- [Depth-First Search and Breadth-First Search in Python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)
- [Difference between BFS and DFS](https://www.thecrazyprogrammer.com/2017/06/difference-between-bfs-and-dfs.html): Non-Visited nodes, Visited nodes, Explored nodes
- [深度优先搜索(DFS)小结](http://x-wei.github.io/dfs-summary.html#for-trees-dfs-with-depth)
- [When is it practical to use Depth-First Search (DFS) vs Breadth-First Search (BFS)?](https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf)