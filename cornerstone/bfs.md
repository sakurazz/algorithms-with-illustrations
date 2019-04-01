# BFS

<center>
<img src="https://i.imgur.com/c0F4gTc.gif" alt="bfs" width="200"/>
</center>

## 基础知识

* BFS visit nodes level by **level** in Graph.
* A node is fully explored before any other can begin.
* Uses **Queue** data structure to store Un-explored nodes.
* BFS is slower and require more **memory**.

Some Application:

* Finding all **connected components** in a graph.
* Finding the **shortest** path between two nodes.
* Finding all nodes within **one** connected component.
* Testing a graph for **bipartiteness**.

## 典型应用 Typical Problems

1. Traversal: 133, 301
2. Connected Components: 200, 261, 323
3. Shortest Path: 🌟[126 word ladder], 127,286, 317, [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
4. Topological 拓扑排序: 207, 269, 444, 631 

## 最佳实践 Best Practice 

**Graph**

``` python
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
``` 

**Connected Component** 

``` python 
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}
```

**Path** 

``` python 
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((next, path + [nxt]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
```

``` python
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']
```

**Shortest Distance**

``` python
# bfs: 1. pop 2. check 3. add unseen neighbors
def neighbor(node):
	return graph[node]

def shortest_depth(graph, start, goal):
	seen, queue = set([start]), [(start, 0)]
	while queue:
		node, depth = queue.pop(0) # deque
		if node == goal: return depth 
		for nxt in neighbor[node] - seen:
			queue.append((nxt, depth+1))
			seen.add(nxt)
	return -1	
```


## 木桩训练

1. 301 Remove Invalid Parentheses 
1. 133 Clone Graph  ❶ 
1. 323 Number of Connected Components in an Undirected Graph
1. 200 Number of Islands
1. 261 Graph Valid Tree ❷
1. 127 Word Ladder 
1. 286 Walls and Gates 
1. 317 Shortest Distance from All Buildings  ❸
1. 207 Course Schedule 
1. 269 Alien Dictionary 
1. 444 Sequence Reconstruction ❹

## Reference 

- [Depth-First Search and Breadth-First Search in Python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)
- [Difference between BFS and DFS](https://www.thecrazyprogrammer.com/2017/06/difference-between-bfs-and-dfs.html): Non-Visited nodes, Visited nodes, Explored nodes
