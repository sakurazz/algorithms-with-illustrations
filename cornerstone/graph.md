# Graph 

## 基础知识

## 典型应用

## 最佳实践

### representation 

* adjacency matrix (effective with **dense** graphs)
* adjacency list (effective with **sparse** graphs)

``` python
# adjacency matrix
matrix = [
[1,1,1]
[1,1,1]
[1,1,1]
]
```

``` python 
# adjacency list 
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
```

## Explain

## Q&A

## Thanks