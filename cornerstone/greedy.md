# Greedy

<img src="https://i.imgur.com/1aDfDOW.png" alt="greedy" width="200"/>


> 做对了，叫**艺高人胆大，四两拨千斤**。
> 做错了，叫一意孤行，执迷不悟。

## 基础知识

source: [wiki](https://www.wikiwand.com/en/Greedy_algorithm)

A greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of **making the locally optimal choice** at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

Greedy algorithms produce good solutions on some mathematical problems, but not on others. Most problems for which they work will have two properties: 

* Greedy choice property
* Optimal substructure



## 典型应用

- prove:
	- stay ahead(induction): [253](https://leetcode.com/problems/meeting-rooms-ii/)
	- exchange argument(deduction): 
	- copy and paste: [135](https://leetcode.com/problems/candy/) 

----

* 可行性，局部最优，不可取消。
	* 可行性：满足问题的约束。
	* 局部最优：看到的目光有限！
	* 不可取消：一旦作出决定，就不再取消。
* 先选择再计算: 44, 134 
* MST: 402, 327, 316 
* Prim vs Kruskal: 达尔文和上帝,  
	* Prim: minheap, 边走边看(自低向上不断试错)
	* Kruskal: UnionFind, 全局(自顶向下精准塑造) , 321   
* 证明：
	* Stay Ahead: 归纳, 435, 452 
	* Exchange Argument: 演绎
	* Copy and Paste: 135 

其他：

- interval: 435, 1024

## 最佳实践

- heap 

## 木桩训练

- [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [135. Candy](https://leetcode.com/problems/candy/)

## Q & A 

## Thanks