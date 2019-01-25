# Shortest path 

## 1. 总结

<br>

|算法 |思想 | 适用情况|时间复杂度|空间复杂度|诞生时间|
|:---|:--- |:---    |:---    |:---    |:--- |   
|BFS|蛮力搜索|不含权重|O(V·E)|O(V·E)|1959|
|Dijkstra|贪心思想|不含负权|O((V+E)logV)|O(E)|1956|
|Bellman-Ford|动态规划|没有限制|O(V·E)|O(E)|1956|



<br>

可以看到，解决问题的范围 Bellman-ford > Dijkstra > BFS(Moore)。

在现实世界中，求最短距离直觉上想到一个方法是`Dijkstra`，**因为「最短」本身就暗示着「贪心」的思路，要先走最短到达下一个点的边。**但是「贪心」思路的重点，在于对于问题已有洞见，所以证明其正确性往往最难说清。但证明错误，一个反例即可：
	
![Dijkstra负权的例子](https://i.imgur.com/wMQwI6H.png)
	
S到A最短距离是2，而用`Dijkstra`，我们得到答案是3，因为从S出发时，我们先贪心选择了A。我们贪心选择的假设是: s→t的最短路一定**不会经过**和`s`距离大于`l(s, t)`的点。在负权图中，我们被上图打了脸。这就像三角形内角和始终是180度，当遇到球面时被打了脸一样。
	
所以为了解决这问题，就需要「动态规划」的思想，因为任何含有`∣V∣`个顶点的图两个点之间的最短路径最多含有`∣V∣−1`条边，那么用`Dijkstra`更新的方式`dist(v)=min{dist(v), dist(u)+l(u,v)}` 去迭代`|V|-1`次就没有问题。当然要说明是，这意味着最短路径不会包含环。理由是，如果是负环，最短路不存在；如果是正环，去掉后变短；如果是零环，去掉后不变。
	
Dijkstra与Bellman-ford也正好说明了`贪心思想`和`动态规划`的区别，`贪心思想`是有了洞见，是先选择再计算，始终由上一步的最优解推导下一步的最优解，而上一部之前的最优解则不作保留；而`动态规划`是先计算再选择，首先找到子问题的最优解，解决子问题，然后找到问题的一个最优解。
	
之外需要注意是: 负！值！圈！（negative-cost cycle）权重总和为负的圈，如果存在这种圈，我们可以在里面滞留任意长而不断减小最短路径长，因此这种情况下最短路径可能是不存在的，可能使程序陷入无限循环。对于 Bellman-Ford 算法来说，判断负值圈存在的方法很简单：`|V|-1`圈后再多迭代一次。因为，如果存在负值圈，那么就会`值`更新。
	
再看看BFS，最简单却很实用的方法，可以说是`Dijkstra`的简化版，因为如果每一条权值相同，即无权图，那么从源(Source)开始访问图(Graph)遇到节点的最小深度就等于到该节点的最短路径，因此Priority Queue就退化成了Queue, `Dijkstra`算法就退化成了BFS。
	
## 2. 练习一下
	
### 2.1 问题是这样子的：
	
There are `n` cities connected by `m` flights. Each fight starts from city `u` and arrives at `v` with a price w.
	
Now given all the cities and fights, together with starting city `src` and the destination `dst`, your task is to find the cheapest price from `src` to `dst` with up to `k` stops. If there is no such route, output `-1`.
	
```
Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
```
![graph](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png)

	
**Note:**
	
- The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
- The size of flights will be in range [0, n * (n - 1) / 2].
- The format of each flight will be (src, dst, price).
- The price of each flight will be in the range [1, 10000].
- k is in the range of [0, n - 1].
- There will not be any duplicated flights or self cycles.
	
	
—— [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)  
	
### 2.2 一个理想思路是：
	
1. 识别出问题是属于求**单源最短路径**系列，算法有三：
	- BFS 
	- Dijkstra 
	- Bellman-Ford 
2. 具体问题具体分析：
	- **有权重**: BFS不适合
	- **没有负边**: Dijkstra可以用，因为每次都最小边走，所以在停K之前，遇到目标节点dst，即得到答案。
	- **最多停K次**: 这个很符合Bellman-Ford的思想出发点：含有`∣V∣`个顶点的图两个点之间的最短路径最多含有`∣V∣−1`条边；所以这里迭代K次即可，然后到目标节点的值即答案。
	
### 2.3 Show me the code 
	
**Bellman-ford algorithm**	

```python
# Time: O(E∗K), where E is the length of flights.
# Space: O(n), the space used to store cur and pre
# Reference: https://leetcode.com/problems/cheapest-flights-within-k-stops/solution/


# Bellman-ford algorithm
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in xrange(2)] # [pre, cur] or [cur, pre]
        dist[0][src] = dist[1][src] = 0
        
        for i in xrange(K+1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)
        
        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1
```



**Dijkstra's algorithm**

``` python 
# Time:  O(E+nlogn), where E is the length of flights
# Space: O(n), the size of the heap 
# Reference: https://leetcode.com/problems/cheapest-flights-within-k-stops/solution/

'''
# Dijkstra's algorithm 
If we continually extend our potential flightpaths in order of cost, we know once we've reached the destination dst that it was the lowest cost way to get there. 
'''
import collections
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        
        best = {} # the best way to get any point 
        pq =[(0, 0, src)] # cost A with B steps to get C
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue 
            if place == dst: return cost 
            
            for nei, wt in graph[place].iteritems():
                newcost = cost + wt 
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost 
                    
        return -1 
```
	

**BFS**

为什么BFS不合适呢？ 

因为BFS是Dijkstra的退化，边的权重限制了BFS在往下一层扩展时，会产生错乱。
	
来看里一个例子：
	
![wrong test](https://i.imgur.com/77GcgcK.jpg)
	
[错误代码](https://repl.it/@WillWang1/787CheapestFlightsWithinKStops-Wrong)在这里，在 front = [1,2], 更新下一层时，就会更新2，从而导致 0->2->3 的答案错误。
	
## 3.再多玩一会
	
1. 【新角度理解算法】试着另一个角度去理解BFS，Dijkstra和Bellman-ford，就是 [Relaxation (iterative method)](https://www.wikiwand.com/en/Relaxation_(iterative_method)) : 参考[wiki](https://www.wikiwand.com/en/Bellman%E2%80%93Ford_algorithm#/Algorithm), 中文称之为「缩放法」？
2. 【抽象能力训练】[818. Race Car](https://leetcode.com/problems/race-car/) : 学会如何把一个问题抽象出最短路径的问题，然后分别用[BFS](https://gist.github.com/WillWang-X/fbcf0ffc2293660bcaec69627931617a) ，[Dijkstra]() 和 [Bellman-ford]() 的思想去解决
3. 【问题扩展】
	- 想想拓扑排序可以用在求最短路径中么？(适用于无环)
	- 那什么时候需要用到多源最短路径呢？如Floyd-Warshall算法
	- 知道 SPFA 和 ASP 么？
	- 检查负环的方法有哪些呢？

## 4.感谢
	
1. [Bellman-Ford in 5 minutes — Step by step example](https://www.youtube.com/watch?v=obWXjtg0L64) 5分钟 Bellman-Ford 算法直觉之旅
2. [带权最短路 Dijkstra, SPFA, Bellman-Ford, ASP, Floyd-Warshall 算法分析](https://www.renfei.org/blog/weighted-shortest-path.html)
3. [图论（二）：图的四种最短路径算法](https://blog.csdn.net/qibofang/article/details/51594673) : Python实现
4. [最短路径问题总结，时间复杂度，空间复杂度对比（JAVA）](https://blog.csdn.net/qq_39630587/article/details/79038849) : 表格总结最短路径问题
5. [最短路径算法总结](http://threezj.com/2016/05/02/%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93/) : Dijkstra //适用于无负权重；Topological sort //适用于无环；Bellman-Ford //适用于无负环



<br>
<br>

简之           
2018.04.17        


## log 

- 2019.01.24: 将笔记从blog移动算法中，系统化

## Todo 

- [ ] Topological sort //适用于无环


