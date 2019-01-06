# Cycle 

![cycle graph](https://i.imgur.com/N3kFuPm.png)

from [Wikiwand:Cycle graph](https://www.wikiwand.com/en/Cycle_graph)


## What is cycle?

> In graph theory, a cycle is a path of edges and vertices wherein a vertex is reachable from itself. 
> 
> from [Wikiwand](https://www.wikiwand.com/en/Cycle_(graph_theory))


## How to detect a cycle in a graph?

### 1. Undirected graph 



从**某个点**出发是否有环

<img src="https://i.imgur.com/oM4AbuB.gif" alt="DFS detect cycle in undirected graph" width=""/>

环的性质: 从某个点出发必然会遇到自己，则成环。

1. DFS: Path中点会遇到自己
2. BFS: 层级会遇到之前的层级



判断**整张图**是否有环

<img src="https://i.imgur.com/jZpDJSq.png" alt="topological vs union-find" width=""/>

环的性质：环中某点必然有**两条**伸出的边。

1. **拓扑**排序: 由多到少，**删**无可删，还有**剩余**，则有环。
2. **并查**集合: 由少到多，遇线则**并**，查到**相同**，则有环。

### 2. Directed graph 


* **某个点**出发是否有环：DFS
* 判断**整张图**是否有环：拓扑排序

Why **NO**? 

![Why BFS and Unoin-find cannot detect cycle in directed graph](https://i.imgur.com/2fCY74a.png)

* 为什么BFS不可行？ 因为BFS的特点是记录层级，而非路径。
* 为什么并查集不行？因为「有向图」环中点，可以只有一条伸出。

## Code 


## 木桩训练

1. [Google面经：判断S点是否一定到D点](https://willwang-x.github.io/2018/02/shift)
2. [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/): 无向环中删一边成树
3. [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/description/): 无向环中删一边成树
4. [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
5. [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
5. [202. Happy Number](https://leetcode.com/problems/happy-number/)
6. [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
7. [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)
8. [457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/)?