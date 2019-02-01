# Union find / disjoint-set 

## 基础知识



## 典型应用

* Find component 
* Detect cycle for the whole graph

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

* 
* 323 Number of Connected Components in an Undirected 