--- 
layout: post
title:  等价思维|终点和环
tags:
- 思路的诞生
status: publish
type: post
published: true
---

<br>

> “看上去是几何问题，实际上是函数问题。” —— 《嫌疑人X的献身》

	
![谷歌面试题](https://i.imgur.com/W9znpVm.jpg)
	
### 1. 问题是这样子的：

给你一个**有向图**Graph，起点S和终点D，问你从起点S出发，不断走，是否**一定会**遇到终点D? 
   
——— Google 面经
	
	
### 2. 一个理想思路是：
	
1. 首先确定这是一个**搜索**问题。
2. **问题转换**: 看似是搜索问题，其实是判断2种情况会返回False：
	- 从**起点**出发遇到**环**
	- 遇到一个**死胡同**点，即点的出度为0。
3. 闪念: 搜索问题可用：DFS, BFS。
4. 而判断有没有环? 三种方法：**拓扑排序，DFS，强连通特性**
5. 问题来了：那用哪一个呢？
	- **拓扑排序**：不好，这是判断整个图有没有环，这里不必，因为如果点不经过，没有意义。(方法是: 每次删除入度为0的点，如果最终图中还有点存在，则有环。)
	- **强连通特性**: 不好，计算量大。这个主要用于发现图中所有的环。这里环的定义是如果存在从点A到点B，也存在点B到点A，那么构成环。
	- **DFS**: 可以啊。利用DFS的特性：记录路径。这里环的定义是**访问过的点是否在之前走过的路径中，如果在，则有环！**
	
<br>
**敲黑板!**

对啊，终于找到一个说明DFS和BFS区别的好例子了：

- **DFS是点扩展**：天生记路径	
- **BFS是面扩展**：天生记层数
	
### 3. Show me the code:
	
<script src="https://gist.github.com/WillWang-X/79010b76d3ec06e975ea939f0a2ec398.js"></script>
	
## 4. 想再玩一会？
	
1. 【等价思维练习】
	- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/) : 再挖掘一下，问题就可以用旧瓶装新酒了(142. Linked List Cycle II)。
	- [237. Delete Node in a Linked List
](https://leetcode.com/problems/delete-node-in-a-linked-list/description/): 如何偷天换柱？想想《嫌疑犯x的献身》
2. 【问题扩展】如何判断一个无向图是否存在环呢? [拓扑排序](http://www.cnblogs.com/TenosDoIt/p/3644225.html)，Union-Find(MST Kruskal就是利用的这个), BFS, DFS 


## 5. 感谢

1. **Credit to Wen Zhong**
2. [Finding all cycles in a directed graph](https://stackoverflow.com/questions/546655/finding-all-cycles-in-a-directed-graph): 利用强连通性找到有向图中所有的环。
3. [Tarjan's algorithm to determine wheter a directed graph has a cycle](https://math.stackexchange.com/questions/917414/tarjans-algorithm-to-determine-wheter-a-directed-graph-has-a-cycle?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

<br>
<br>

简之           
2018.02.18

<br>
<br>
<br>
<br>

## ChangeLog

- 2018.04.16: 
	1. 删除不理想答案: 和Wen讨论，BFS不方便判断有向图环的判断，因为此题判断环(即访问过的点是否出现过在之前的路径上)是路径依赖的，而BFS不方便解决这个问题，同时此题适合Recursive，因为Stack可以刻画路径。
	2. 添加无向图的环的判断。
- 2018.01.04 
	- 为什么BFS在这里不能判断环？因为这是「有向图」。