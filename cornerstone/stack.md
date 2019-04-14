# Stack 

![stack](https://i.imgur.com/lrLuOE0.gif)


> when to pop and push?
> 
> **Stack** is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

## 基础知识

Learn to recognize when the stack **LIFO** property is applicable. For example, **parsing** typically benefits from a stack. 

Consider augmenting the basic stack or queue data structure to support additional operations, such as **finding the maximum element**. 

### core

- [ ] the typical use of stack can be abstracted into a depth-first walk?

## 典型应用


- LIFO: 901
- **nearest largest**: 84, 85, 801, 739, 907, 221, 1019 (7 solved in 1 way)
- save for later:
- top-down (DFS?): 
- special order:

## 最佳实践

``` python 
# to maintain an order in the stack (= save for later)
# e.g. LC1019, nearest largest 
def compare():
	pass 
	
def deal():
	pass
	
for i, num in enumerate(input):
	while stack and compare(num, stack[-1]):
		# hit the bottom 
		last = stack.pop()
		deal(last, input)
	stack.append(i)
```

## 木桩训练

* [155. Min Stack](https://leetcode.com/problems/min-stack/) 🌟
* [84.Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (系列, 907 + 42? 85, 901, 907, 739)
* [907.Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) 
* [94.Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) (Iterative, 系列)!  pre-order, 394 🌟
* [232.Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
* [770.Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) (系列)
* [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) 🌟

## Explain

## Q & A

1. stack 和 heap 有什么区别？
	- 都在维持某种顺序，而stack通过pop()和push()完成，而heap需要进入容器之后二次处理得到。
2. stack的优化有什么？
	- 如果不关注过程，只在乎结果。可以使用变量`count`来标记，空间由`O(n)`到`O(1)`, 如[LC 1021](https://leetcode.com/problems/remove-outermost-parentheses/), 请试着用stack和count分别解决。是不是有一种在DP中，二维cache压缩成一维的感觉。

## More

- [Stack and Queue, Why?](https://stackoverflow.com/questions/2074970/stack-and-queue-why): DFS + stack, BFS + queue	