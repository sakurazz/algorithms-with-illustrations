## Granularity：Zoom out - 918

![granularity](https://i.imgur.com/I52hpmu.jpg)

> 在人类历史早期，人们会把像硫酸，食盐，葡萄糖这样外观纯净，成分单一，性质稳定，应用广泛的液体或者晶体误认为单质，直至近代才知道它们是化合物，可以分解为氢，氧，硫，碳等化学元素。而一旦人类的认知到达了这个层次，就立刻开始利用这些元素合成一些自然界中原先不存在的化合物，化学学科本身的理论水平也就不可同日而语了。 —— 《元素模式》


## 1. 

对于同一个问题，所看到的**问题颗粒度**的不同，会得到不同的思路。就如我常看到的电视屏幕，我们的视角是一个不同颜色的画面，但是你切入到更小的视角，整个画面是只是“红蓝绿“三原色的变化。

![How a TV Works in Slow Motion - The Slow Mo Guys](https://i.imgur.com/SmXhQpI.gif)

就如[918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/description/)这道题，我看到的可以是组成的`list`的一个个数字作为单位, 或者整个`list`作为单位，有什么区别么？

如果问题的对象是前者，我会想到的解法，是遍历一个个元素，想着如何在过程中保存最大值。所以想到把两个`list`组装成一个新的`list`。

但是如果是后者，我们可能想到问题的解: 
	A. 要么是`list`中间的subarray组成的解，即[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)的解， 
	B. 要么是`list`两边subarray组成的解，即问题转换成求 Minimum subarray = B

![A or B](https://i.imgur.com/uSK9bUR.png)
	
答案则是 res = max(A,	sum(list) - B)

从这个抽象层次去想这道问题，我们就可以复用53求Maximum Subarray函数。

## 小结

这是解题切入角度，我把其归结为“问题的颗粒度”的思考，可能不太准确，期待想到更好的总结题。但其本质应该是**抽象能力**和**问题reduce的能力**。