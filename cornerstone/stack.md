# Stack 

![stack](https://i.imgur.com/W0LDr8g.png)


> when to pop and push?
> 
> **Stack** is a linear data structure which follows **a particular order** in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

## 基础知识

Learn to recognize when the stack **LIFO** property is applicable. For example, **parsing** typically benefits from a stack. 

Consider augmenting the basic stack or queue data structure to support additional operations, such as **finding the maximum element**. 

### core

- [ ] the typical use of stack can be abstracted into a depth-first walk?

## 典型应用


- LIFO: 901
- **nearest largest**: 84, 85, 801, 739, 907, 221, 1019 (7 solved in 1 way)
- save for later:
- top-down (DFS-style?): 
- special order:

## 最佳实践

### general (DFS style)

``` python 
# to maintain an order in the stack (= save for later)
# e.g. LC1019, nearest largest 
for i, num in enumerate(input):
	# base case 
	while stack and compare(num, stack[-1]):
		# hit the bottom 
		last = stack.pop()
		# caculate...
	# general case 
	stack.append(i)
```

### dummy value 

``` python
def largest_rectangle_area(self, heights: List[int]) -> int:
    heights.append(0)             # dummy value 
    stack = [(float("-inf"), -1)] # dummy value: val, pos 
    ans = 0
    for i, num in enumerate(heights):
        while num < stack[-1][0]: # no while stack and ...
            h = stack.pop()[0]
            w = i - stack[-1][1] - 1
            ans = max(ans, h * w)
        stack.append((num, i))
    return ans
```

### save for later 

``` python
def decode_string(self, s: str) -> str:
    stack = []
    for i, char in enumerate(s):
        if char == "]":
            letters = ""
            while stack and stack[-1] != "[":
                letters = stack.pop() + letters
            stack.pop() # pop "["
            digits = ""
            while stack and stack[-1].isdigit():
                digits = stack.pop() + digits 
            stack.append(int(digits) * letters)
        else:
            stack.append(char)
    return "".join(stack)
```

```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "10[a]", return "aaaaaaaaaa".
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