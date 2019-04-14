# Union find / disjoint-set 

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