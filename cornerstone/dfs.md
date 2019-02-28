
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

- permutation: [46](https://repl.it/@WillWang42/permute)
- detect cycle: [google](https://willwang-x.github.io/2018/02/shift)
- connected component: 924, 928
- **path**
- Topology Sort
 

## 最佳实践

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
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
```

**Recursive**

```python
def dfs(graph, start, visited=set()):
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited

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
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for nxt in graph[start] - set(path):
        yield from dfs_paths(graph, nxt, goal, path + [nxt])

list(dfs_paths(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
```

## Q&A

### DFS vs Backtracking

* [Backtracking](https://www.wikiwand.com/en/Backtracking) is a more general purpose algorithm.
* [Depth-First search](https://www.wikiwand.com/en/Depth-first_search) is a specific form of **backtracking** related to searching tree structures. 

> One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch before backtracking.

It uses backtracking as part of its means of working with a tree, but is limited to a tree structure.

Backtracking, though, can be used on any type of structure where portions of the domain can be eliminated - whether or not it is a logical tree. The Wiki example uses a chessboard and a specific problem - you can look at a specific move, and eliminate it, then backtrack to the next possible move, eliminate it, etc.

from [What's the difference between backtracking and depth first search?](https://stackoverflow.com/questions/1294720/whats-the-difference-between-backtracking-and-depth-first-search)







## 木桩训练 

* [112. Path Sum](https://leetcode.com/problems/path-sum/submissions/1)
* [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
* [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)
* [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)
* [851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/description/)
* subset


## Thanks 

- [Depth-First Search and Breadth-First Search in Python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)
- [Difference between BFS and DFS](https://www.thecrazyprogrammer.com/2017/06/difference-between-bfs-and-dfs.html): Non-Visited nodes, Visited nodes, Explored nodes
- [深度优先搜索(DFS)小结](http://x-wei.github.io/dfs-summary.html#for-trees-dfs-with-depth)