# Aogrithms' Delight 😇 


| Ⅰ | Ⅱ | Ⅲ | Ⅳ | Ⅴ |
| :--------: | :---------: | :---------: | :---------: | :---------: | 
| 问题类型<br>[❓](#常见问题) | 数据结构<br>[⛓](#数据结构)|核心思想<br>[🤖](#核心思想) | 实现技巧<br>[✍️](#实现技巧) | Reference<br>[📝](#reference) |

<br>
> Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.  
> <br>
> —— *Master Sun: The Art of War*

<br>


## 清单 Lists

| 关键词 🔑 | 典型题 👻 | 讲解 🎦 | 笔记 📒 | 备注  |
| :--------: | :---------: | :---------: | :---------: | :---------: | 
| Data Strcture| ---- | ---- | ---- | ---- |
| Array Queue|  |  | |
| Array Stack|[678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/) |  | |
| Linked List| 25,141, 206, | [25](https://youtu.be/W0QkqzwB9qY) | | 增删查改转; Dummy node, reverse, |
| Tree Heap | [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/description/) | [407](https://youtu.be/7niUr7LlviY) | [heap-407](https://github.com/WillWang-X/algorithms-delight/blob/master/cornerstone/heap-trapping-rain-water-II.ipynb) | [] BFS solution |
| Tree Trie| [208] |  | |
| Segement Tree| [218] |  | |
| Binary Indexed Tree|  |  | |
| Tree Traversal |  |  | |
| Undirected Graph|  |  | |
| Directed Graph|  |  | |
| MST |  |  | |
| Shortest Path| [787] ,[505] |  | |
| String|  |  | |
| Two Pointer|  |  | |
| Sliding Window| 76 |  | |
| Matrix|  |  | |
| Hash| 146 |  | |
| Two Sum系列|  |  | |
| 算法思想| ❤️ | ❤️ | ❤️ | ❤️|
| Sorting|  |  | |
| DFS|  |  | |
| BFS|  |  | |
| Binary Search | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/) | [33](https://youtu.be/Rmny73Wx3D0) | [?] | 减治系列 |
| DP |  |  | |
| 股票系列 |  |  | |
| Greedy |  |  | |
| Recursion |  |  | |
| Backtracking |  |  | |
| 思维方式 | ---| --- | --- | --- | 
| Reverse	thinking | 88， 795 |  | |
| Definition| 261 |  | |
| Object| 418 |  | |
| 双标准| 678 |  | |
| 满足/不满足| 836 |  | |


## CheatSheet 

### Linked List 

List problems often have a simple brute-force solution that uses 0(n) space, but a subtler solution that uses **the existing list nodes** to reduce space complexity to 0(1). 

Very often, a problem on lists is conceptually simple, and is more about **cleanly coding what's specified**, rather than designing an algorithm.

Consider using **a dummy head** (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely. 

It's easy to forget **to update next** (and previous for double linked list) for the head and tail.

Algorithms operating on singly linked lists often benefit from using **two iterators**, one ahead of the other, or **one advancing quicker than the other**. 
 
#### Key words 
- deletion O(1): moditfy the value or pointer 
- dummy node: 
- reverse: [25](https://leetcode.com/problems/reverse-nodes-in-k-group/description/), [92](https://leetcode.com/problems/reverse-linked-list-ii/description/), [206](https://leetcode.com/problems/reverse-linked-list/description/)
- partition: merge two lists
- linked list ~= array 
- two pointer (fast/slow pointers)
	- get the kth from last node 
	- detect cycle 
	- getting the middle node 

#### Corner cases
- Single node 
- Two nodes
- Linked list has cycle. Clarify with the interviewer whether there can be a cycle in the list. Usually the answer is no.


## 常见问题❓

### 基础问题

- Big O notation

### 问题分类
- 遍历问题
	- 树的遍历：增删查改，前，中，后序
	- 图的遍历：最小生成树？
- 查找问题
	- 字符串的查找： 
		- O(1) 查找？
		- 子串查找？
	- 树的查找：环? 
	- 图的查找：环? 最短路径?
- 排序问题
	- 拓扑排序 
- 位操作
- 组合问题
- 集合问题
- 数值问题

## 数据结构⛓

- 数据**逻辑**结构
	- 线性结构
		- 线性表(数组和链表)
		- FIFO: 队列 
		- FILO: 栈
	- 非线形结构
		- 树
			- Heap  	
			- BST
			- Trie 
			- Binary Indexed Tree
			- Segment Tree 
		- 图 
			- 有向图
			- 无向图 	
- 数据**存储**结构
	- 顺序存储(e.g. 字符串)
	- 链式存储(e.g. 链表)
	- 索引存储(e.g. 数组)
	- 散列存储(e.g. 哈希表)

## 核心思想🤖

- 蛮力算法
	- 选择排序和冒泡排序
	- DFS & BFS
- 分而治之
	- 二分查找：BS，BST
- 动态规划
- 贪心算法
- 减而治之
	- 合并排序
	- 快速排序
- 变而治之
	- 预排序
	- 堆排序


## 实现技巧✍️

- 递归和迭代
- 双指针：追逐，相遇，呼应
- 时空权衡
	- 预处理
	- 散列法
- 排序算法
- 元素视角：操作对象的转移
- 正反思维：左右，等价



## Reference 

- [题目训练](https://leetcode.com/problemset/algorithms/)
- [模拟面试](https://www.pramp.com/dashboard#/)
- [Github使用指南:把Github当作博客用](https://github.com/mqyqingfeng/Blog/issues/2)
- *Elements of Programming interviews*