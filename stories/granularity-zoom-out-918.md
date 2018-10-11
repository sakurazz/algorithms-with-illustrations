## Granularity：Zoom out - 918

![granularity](https://i.imgur.com/I52hpmu.jpg)

> 在人类历史早期，人们会把像硫酸，食盐，葡萄糖这样外观纯净，成分单一，性质稳定，应用广泛的液体或者晶体误认为单质，直至近代才知道它们是化合物，可以分解为氢，氧，硫，碳等化学元素。而一旦人类的认知到达了这个层次，就立刻开始利用这些元素合成一些自然界中原先不存在的化合物，化学学科本身的理论水平也就不可同日而语了。 —— 《元素模式》


## 1. 问题是这样子的

Given **a circular array C** of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


```
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```

```
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
```

-- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/description/)
## 2. 一个理想的思路是

对于同一个问题，所看到的**问题颗粒度**的不同，会得到不同的思路。就如我常看到的电视屏幕，我们的视角是一个不同颜色的画面，但是你切入到更小的视角，整个画面是只是“红蓝绿“三原色的变化。

![How a TV Works in Slow Motion - The Slow Mo Guys](https://i.imgur.com/SmXhQpI.gif)

就如918这道题，我看到的可以是组成的`list`的一个个数字作为单位, 或者整个`list`作为单位，有什么区别么？

如果问题的对象是前者，我会想到的解法，是遍历一个个元素，想着如何在过程中保存最大值。所以想到把两个`list`组装成一个新的`list`。

但是如果是后者，我们可能想到问题的解: 
	A. 要么是`list`中间的subarray组成的解，即[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)的解， 
	B. 要么是`list`两边subarray组成的解，即问题转换成求 Minimum subarray = B

![A or B](https://i.imgur.com/uSK9bUR.png)
	
答案则是 res = max(A,	sum(list) - B)

从这个抽象层次去想这道问题，我们就可以复用53求Maximum Subarray函数。

## 3. Show me the code 
```python 
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """        
        if max(A) < 0:
            return max(A)
        
        # Case 1:  middle
        max_middle = self.max_subarray(A) 

        # Case 2: two sides
        max_sides = sum(A)
        A = [-A[i] for i in range(len(A))]
        max_sides += self.max_subarray(A) 

        # The maximum circular sum will be maximum of two sums 
        return max(max_middle, max_sides)
        
    def max_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)

        l_max, g_max = 0, 0
        for i in nums:
            l_max += i
            g_max = max(l_max, g_max)
            l_max = max(0, l_max)
        return g_max
```

## 4.小结

这是解题切入角度，我把其归结为“问题的颗粒度”的思考，可能不太准确，期待想到更好的总结题。但其本质应该是**抽象能力**和**问题reduce的能力**。


## 5. Thanks
- [交互水深 03 | 理解 [ 用户任务 ] 的 [ 颗粒度 ]](https://zhuanlan.zhihu.com/p/33175126)
- [How a TV Works in Slow Motion - The Slow Mo Guys](https://www.youtube.com/watch?v=3BJU2drrtCM)