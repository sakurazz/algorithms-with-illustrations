# Union find / disjoint-set 

![union-find](https://camo.githubusercontent.com/c885a811800fc105c74f5584aacaecfb1305e327/68747470733a2f2f692e696d6775722e636f6d2f4f6c64556661312e6a7067)

## 基础知识

source: [wiki](https://www.wikiwand.com/en/Disjoint-set_data_structure)

In computer science, a disjoint-set data structure (also called a `union–find` data structure or merge–find set) is a data structure that **tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets**. It provides near-constant-time operations (bounded by the inverse Ackermann function) to add new sets, to merge existing sets, and to determine whether elements are in the same set. In addition to many other uses (see the Applications section), disjoint-sets play a key role in Kruskal's algorithm for finding the minimum spanning tree of a graph.


## 典型应用

* Find component 
* Detect cycle for the whole graph
* MST

## 最佳实践?

``` python
# https://repl.it/@WillWang42/union-find

class unionFind:

  def __init__(self, N):
    self.parents = [i for i in range(N)]
    self.ranks = [0 for _ in range(N)]
    self.components = N
  
  def find(self, x):
    if self.parents[x] == x:
      return x 
    return self.find(self.parents[x])
       
  def union(self, x, y):
    x_parent = self.find(x)
    y_parent = self.find(y)
  
    if x_parent != y_parent:
      if self.ranks[x_parent] > self.ranks[y_parent]:
        self.parents[y_parent] = x_parent
      elif self.ranks[x_parent] < self.ranks[y_parent]:
        self.parents[x_parent] = y_parent
      else:
        self.parents[x_parent] = y_parent
        self.ranks[x_parent] += 1
      self.components -= 1
```  

## 木桩训练

* 323 Number of Connected Components in an Undirected 

## Q&A

### 1. Union-Find or DFS: which one is better to find connected component?

> tl;dr - Static graph? DFS! Dynamic graph? Union-find!

The union-find algorithm is best suited for situations where the equivalence relationship is changing, i.e., there are "Union" operations which need to be performed on your set of partitions. Given a fixed undirected graph, you don't have the equivalence relationships changing at all - the edges are all fixed. OTOH, if you have a graph with new edges being added, DFS won't cut it. While DFS is asymptotically faster than union-find, in practice, the likely deciding factor would be the actual problem that you are trying to solve.

source: [stackoverflow](https://stackoverflow.com/questions/28398101/union-find-or-dfs-which-one-is-better-to-find-connected-component)
