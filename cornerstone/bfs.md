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

## 典型应用

1. Traversal: 133, 301
2. Connected Components: 200, 261, 323
3. Shortest Path: 🌟[126 word ladder], 127,286, 317, [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
4. Topological 拓扑排序: 207, 269, 444, 631 

## 最佳实践

- connected component 
- path
- shortest distance
- traverse layer by layer(depth)

**Graph**

``` python
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
``` 

### connected component 

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

### path

``` python 
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))

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

### shortest distance

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

### traverse layer by layer 

``` python
front = [start]
depth = 0
while front:
	nxt = []
	for node in front:
		for child in children(node):
			nxt.append(child)
	front = nxt 
	depth += 1	
```

``` python
seen, targets = set(), set()
queue = [(node, 1) for node in seen]
for node, depth in queue:
    if node in targets: return depth
    for nei in graph[node]:
        if nei not in seen:
            seen.add(nei)
            queue.append((nei, depth+1))
```

- Try [815](https://leetcode.com/problems/bus-routes/)

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
2. [815. Bus Routes](https://leetcode.com/problems/bus-routes/)

## Q&A

### 1. BFS 和 Dijsktra 的关系？

Edge == 1, Dijsktra 退化成 BFS。因为如果每一条权值相同，即无权图，那么从源(Source)开始访问图(Graph)遇到节点的最小深度就等于到该节点的最短路径，因此Priority Queue就退化成了Queue, `Dijkstra`算法就退化成了BFS。

- [787. Cheapest Flights Within K Stops
](https://leetcode.com/problems/cheapest-flights-within-k-stops/): BFS is not a good choice
- [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/): use BFS instead Dijkstra

## Reference 

- [Depth-First Search and Breadth-First Search in Python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)
- [Difference between BFS and DFS](https://www.thecrazyprogrammer.com/2017/06/difference-between-bfs-and-dfs.html): Non-Visited nodes, Visited nodes, Explored nodes
