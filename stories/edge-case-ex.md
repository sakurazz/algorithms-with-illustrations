# Edge case / corner case 如何处理？

- [ ] 补充Interview 现场的讨论方式
- [ ] 补充 二分法找到middle的思考背后， middle = left + (right - left) / 2 

> 对于edge case，
> 
> - 表现平庸：完全意识不到，不做任何检查
> - 符合预期：利用语言和数据结构纠错
> - **超出预期**：**进行额外的边界条件检查**
> 
> -- *[“应聘者面试中犯错了，我是否该提醒”](https://mp.weixin.qq.com/s?__biz=MjM5NTQ1NTE4Ng==&mid=2247483749&idx=1&sn=68fcd5f4750bd2d73f728bf1a4c05182&chksm=a6f908d8918e81ce87b3a9a604ca5efe183a49eab5526e195d6c457c3b02a7c4d48185602874&mpshare=1&scene=1&srcid=1006nJGM0E9AiauNU0DcMzVG%23rd)*
> 

## 1. What is edge case / corner case ?

- **Edge case** occurs at an extreme (maximum or minimum) operating parameter.
- **Corner case** occurs outside of normal operating parameters, specifically when multiple environmental variables or conditions are simultaneously at extreme levels, even though each parameter is within the specified range for that parameter. (The "outside normal operating parameters" obviously means something like "outside typical combination of operating parameters", not strictly "outside allowed operating parameters". That is, you're still within the valid parameter space, but near its corner.)
- **Boundary case** occurs when one of inputs is at or just beyond maximum or minimum limits.
- **Base case** is where Recursion ends.

## 2. Edge case 考虑哪些有哪些？

- None, []
- n = 0 or 1 where n = len(nums)  e.g. LC 238
- Negative, e.g. LC53

## 3. best practice when interview 

- 在写代码前，和面试官讨论可能的edge case的情况 (补充具体的讨论方式)
- 在写完代码后，测试各种典型test cases, 如 [], [1], [-1]


## 4. 树桩训练

- [238. Product of Array Except Self](https://leetcode.com/problemset/all/): 考虑 n = 0 or 1 
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/): 考虑 [-4, -3, -2, -1] 全是负数 和 [] 


## 5. Thanks 

- [“应聘者面试中犯错了，我是否该提醒”](https://mp.weixin.qq.com/s?__biz=MjM5NTQ1NTE4Ng==&mid=2247483749&idx=1&sn=68fcd5f4750bd2d73f728bf1a4c05182&chksm=a6f908d8918e81ce87b3a9a604ca5efe183a49eab5526e195d6c457c3b02a7c4d48185602874&mpshare=1&scene=1&srcid=1006nJGM0E9AiauNU0DcMzVG%23rd)
- [What are the difference between an edge case, a corner case, a base case and a boundary case?](https://softwareengineering.stackexchange.com/questions/125587/what-are-the-difference-between-an-edge-case-a-corner-case-a-base-case-and-a-b)