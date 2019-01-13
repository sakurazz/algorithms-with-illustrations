# Cheat sheet for algorithm 

> Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.  —— *The Art of War*


| Ⅰ | Ⅱ | Ⅲ | Ⅳ | Ⅴ |
| :--------: | :---------: | :---------: | :---------: | :---------: | 
| 问题类型<br>[❓](#常见问题) | 数据结构<br>[⛓](#数据结构)|核心思想<br>[🤖](#核心思想) | 实现技巧<br>[✍️](#实现技巧) | Reference<br>[📝](#reference) |

## Content 

- Binary 
- String/Array: KMP
- Linked list
- Queue
- Stack 
- Heap 
- Tree: MST/Traverse
- Binary Tree 
- Binary Search Tree
- Trie 
- Segment Tree
- Binary Indexed Tree
- Graph
- Hash Map
- Union-Find 
- Binary Search 
- Backtracking 
- Recursion 


## Queue [FIFO]

### Study notes

### Notes

### key words

### Corner cases





## BST 

### Study notes

### Notes
 With a BST you can **iterate** through elements in sorted order in time 0(n) (regard- less of whether it is balanced). 
 
Some problems need **a combination of a BST and a hashtable**. For example, if you insert student objects into a BST and entries are ordered by GPA, and then a student's GPA needs to be updated and all we have is the student's name and new GPA, we cannot find the student by name without a full traversal. However, with an additional hash table, we can directly go to the corresponding entry in the tree. 

Sometimes, it's necessary to **augment** a BST, e.g., the number of nodes at a subtree in addition to its key, or the range of values sorted in the subtree. 

The BST property is **a global property**—a binary tree may have the property that each node's key is greater than the key at its left child and smaller than the key at its right child, but it may not be a BST. 

### key words
- inorder [285](https://leetcode.com/problems/inorder-successor-in-bst/description/), [230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)
- BST & Hashtable
- subtree






## Binary Indexed Tree 

### Study notes

### Notes

### key words

### Corner cases

## Graph 

### Study notes

### Notes
 It's natural to use a graph when the problem involves **spatially connected** objects, e.g., road segments between cities. 
  
More generally, consider using a graph when you need to analyze **any binary relationship**, between objects, such as interlinked webpages, followers in a social graph, etc. 

Some graph problems entail **analyzing structure**, e.g., looking for cycles or connected components. DFS works particularly well for these applications. 

Some graph problems are related to **optimization**, e.g., find the shortest path from one vertex to another. **BFS, Dijkstra's shortest path algorithm, and minimum spanning tree** are examples of graph algorithms appropriate for optimization problems. 

### key words
- DAG 

### Corner cases



## Backtracking 


[A general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum, Palindrome Partioning)](https://leetcode.com/problems/permutations/discuss/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning)

### Study notes

基本概念：
backtracking（回溯算法）也叫试探法，它是一种系统地搜索问题的解的方法。回溯算法的基本思想是：从一条路往前走，能进则进，不能进则退回来，换一条路再试。

回溯算法说白了就是穷举法。不过回溯算法使用剪枝函数，剪去一些不可能到达最终状态（即答案状态）的节点，从而减少状态空间树节点的生成。 
回溯法是一个既带有系统性又带有跳跃性的的搜索算法。它在包含问题的所有解的解空间树中，按照深度优先的策略，从根结点出发搜索解空间树。算法搜索至解空间树的任一结点时，总是先判断该结点是否肯定不包含问题的解。如果肯定不包含，则跳过对以该结点为根的子树的系统搜索，逐层向其祖先结点回溯。否则，进入该子树，继续按深度优先的策略进行搜索。

回溯法在用来求问题的所有解时，要回溯到根，且根结点的所有子树都已被搜索遍才结束。
而回溯法在用来求问题的任一解时，只要搜索到问题的一个解就可以结束。
这种以深度优先的方式系统地搜索问题的解的算法称为回溯法，它适用于解一些组合数较大的问题。


### Notes

### key words
- combination: 39 
- permutation 46 

### Corner cases




## Recursion 

### Study notes

Recursion is especially suitable when **the input is expressed using recursive rules.** 

Recursion is a good choice for **search, enumeration, and divide-and-conquer.** 

Use recursion as **alternative to deeply nested iteration loops**. For example, recursion is much better when you have an undefined number of levels, such as the IP address problem generalized to k substrings. 

If you are asked to **remove recursion** from a program, consider mimicking call stack with the **stack data structure**.

Recursion can be easily removed from a **tail-recursive** program by using a while- loop—no stack is needed. (Optimizing compilers do this.) 

If a recursive function may end up being called with **the same arguments** more than once, cache the results—this is the idea behind Dynamic Programming.

### Notes
- tree: [687 Path](https://leetcode.com/problems/longest-univalue-path/description/)
- enumeration: [78], [248]

### key words
- all A[A[x:i] > A[i]: 

### Corner cases




----
## xxxxx

### Study notes

### Notes

### key words

### Corner cases






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