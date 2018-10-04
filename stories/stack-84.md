# Stack: 回眸一笑，原来是你

> Linear lists in which insertions, deletions, and accesses to values occur almost always at the first or the last node are very frequently encountered, and we give them special names . . . 
> 
> —"The Art of Computer Programming, Volume 1,"  D. E. KNUTH, 1997


	
## 1. 故事是这样子：
	
Weekly Contest 做了 907. Sum of Subarray Minimums, 事后发现其核心部分, "找左右边界" 其实就是上一周的 901 Online Stock Span 简单变形。解法是相同的。但是 901 秒出，而 907 却花了一些时间。后来发现，901 和 739. Daily Temperatures 也是换了背景，内核是一样的题。
	
然而，在研究一道旧题：85. Maximal Rectangle. 发现其可以 压缩成一维, 变成 84. Largest Rectangle in Histogram。
	
就像你猜到的一样, 84 和 907 其实是同一种做法，“找左右边界”的方法完全可以复用。但是换了衣服的题目，确实没有一眼看出来。细细一想，惊叫："题目是一样的"。 所谓，书有薄而厚，再**由厚而薄**。写代码，一样！
	
## 2. 本质是什么？
	
所以，这些题的本质是什么呢？他们本质都在求 **离我最近比我大或者小数的位置**, 然后都用了stack, 核心是什么让你想到使用Stack呢？ 
	
我的解答是：**回眸一笑，原来是你。**
	
什么意思呢？一图胜千言。
	
![901](https://i.imgur.com/Cg3x69B.png)
	
解释一下：
	
以901为例，我想要的效果是：**回头抬望，第一眼即是你。** 

说人话就是，遍历数组的时，需要后进先出，即Stack的特性，往回查找，把哪些比我小的都Pop出来，因为对下一个要遍历的数来说，不会再用到。

以 75 为例， 前面三个数 [60, 70, 60] 都比75小，所以我们得到 (75, 4), 包括75自己。当下一个数85, 与stack[-1]比较，85 > 75, 那么必然比 [60, 70, 60], 所以无须存他们的信息。所以，此时 stack 应该是

>[(100, 1), (80,1), (75, 4)]
	
## 3. 小结
	
**离我最近比我大或者小数的位置** 可以总结为“Save for later”问题, 保留有用信息，便于之后读取。类似的问题就是括号系列问题，如 678. Valid Parenthesis String. 其他关于stack使用场景还有
	
- 特殊顺序, 如 232. Implement Queue using Stacks
- 用栈解决自上而下结构的问题: 利用栈数据结构消除递归 如 94. Binary Tree Inorder Traversal (Iterative)


## 4. 木桩训练

* [84.Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (系列, 907 + 42?)
* [907.Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) 
* [94.Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) (Iterative, 系列) 
* [232.Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
* [770.Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) (系列)
	