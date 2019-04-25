# 928 Minimize Malware Spread II


```
Input: graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
Output: 1
```
![](https://i.imgur.com/ybqXuWt.png)


题目，本质上得到一个排序，而这个排序是: 求得感染点`I`能够感染的`唯一点O`的数量，`唯一点O`指`O`只被`I`感染, 没有通过其他点。

``` markdown 
`node`: the node that is derected infected by `I`
`2`: [1] 
`3`: [1]
```

## Code 

### Version 0.1

``` python 
# Time Limit Exceeded
class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        N = len(graph)
        clean = set(range(N)) - set(initial)
        
        def dfs(u, visited, malware):
            for v, is_adj in enumerate(graph[u]):
                if is_adj and v not in visited:
                    visited.add(u)
                    if v not in clean:
                        malware.add(v)
                    else:
                        dfs(v, visited, malware)

        scores = {}
        for u in clean:
            visited, malware = set(), set()
            dfs(u, visited, malware)
            if len(malware) == 1:
                m = malware.pop()
                scores[m] = scores.get(m, 0)  + 1
        
        best_m, best_s = min(initial), -1
        for m, score in scores.items():
            if score > best_s or (score == best_s and m < best_m):
                best_m, best_s = m, score
        return best_m        
```

### Version 0.2 

```python 
class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        N = len(graph)
        clean = set(range(N)) - set(initial)
        
        def dfs(u, seen):
            # [1, 0, 1, 0]
            for v, is_adj in enumerate(graph[u]):
                if is_adj and (v in clean) and (v not in seen):
                    seen.add(v)
                    dfs(v, seen)
                    
        infected_by = {v: [] for v in clean}
        for u in initial:
            seen = set()
            dfs(u, seen)
            for v in seen:
                infected_by[v].append(u)
            
        contribution = collections.Counter()
        for v, malware in infected_by.items():
            if len(malware) == 1:
                contribution[malware[0]] += 1
        
        best = (-1, min(initial))
        for u, score in contribution.items():
            if score > best[0] or (score == best[0] and best[1] > u):
                best = (score, u)
        
        return best[1]
```

### Version 0.3

``` python
class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        self.initial_set = set(initial)
        
        def find_component(x, visited):
            visited.add(x)
            for nxt, is_connected in enumerate(graph[x]):
                if is_connected and nxt not in visited:
                    find_component(nxt, visited)
            return visited
        
        def affected_by(x):
            count = 0 
            for nxt, is_connected in enumerate(graph[x]):
                if is_connected and nxt != x:
                    component = find_component(nxt, visited = {x})
                    if len(component & self.initial_set) == 1:
                        count += len(component)
            return count 
            
        removed, affected = min(initial), affected_by(min(initial))
        for x in initial:
            count = affected_by(x)  
            if count > affected:
                removed, affected = x, count
        return removed       
```
