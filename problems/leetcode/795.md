--- 
layout: post
title:  左右之分
tags:
- 思路的诞生
status: publish
type: post
published: true
---

<br>

> 很多事情，不是高下之分，它无非是左右之分。 —— 颜如晶

### 1.问题是这样子的：

We are given an array A of positive integers, and two positive integers L and R (L <= R). 

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

```
Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

**Note:** 

*  L, R  and A[i] will be an integer in the range [0, 10^9].
*  The length of A will be in the range of [1, 50000].

—— 795. Number of Subarrays with Bounded Maximum

### 2.一个理想的思路是：

1. 看到关键词subarray想到得到在一个list中划定范围，叮！Sliding window，一首一尾。
2. 定睛再看，并没有要极值，而是要求所有个数，Sliding window限制条件就不太好用了。
3. 那就要找到一个数的方式：能穷尽而不会遗漏。
	- 左对齐：以某个数为开始的最长子串。
	- 右对齐：以某个数为结尾的最长子串。
4. 然后求这个子串能构成的有效个数。
	- 以首去数，要注意，**`小小中`**不行。
	- 以尾去数，要注意，要记录之前遇到的**“小”**的个数。

真正去实现的时候，你会发现右对齐去数数会比左对齐更快。
	
	
![笔记记录](https://i.imgur.com/YhvhZ1V.jpg)

### 3. Show me the code

<script src="https://gist.github.com/WillWang-X/3237a2b83578158c196226b7cebe8818.js"></script>

### 4. 想再玩一会？

1. 如果「减治」的思想去做这道题，你会有什么想法呢？
2. [456. 132 Pattern](https://leetcode.com/problems/132-pattern/)：对这道题的你会什么新的启发呢？
3. [413. Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/description/):在list中让你数个数，为了避免重复数，都可以左对齐，或者右对齐去数。

### 5. 感谢

- Master Zhao 
- Yingda Zheng 
	

<br>
<br>

简之           
2018.03.05
