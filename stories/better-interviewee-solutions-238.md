# 面试中更好的解法选择

## 1. 面试中的算法选择

- Brute force first
- Easier to explain, avoid premature optimization

## 2. 实战例子

一次面试中，遇到了 238. Product of Array Except Self。 

最优解的做法是：

``` python 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or n == 1:
            return []
        
        result = [None for _ in range(n)]
        
        product = 1
        for i in range(n):
            result[i] = product 
            product *= nums[i]
        
        product = 1
        for i in range(n-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        
        return result 
```

但是这不容易一两句话解释, 首先上来应该先说最直白的解法，

**A brute force approach** would be to use two nested loops: for each index `i` in `arr[i]`, loop over `arr` while multiplying all the other values and place the result in the ith element of the new array.

This gives us an O(N^2) time complexity. We can do better.

这时候可以使用取得所有数的积，然后除以每一个数，得到答案。这样会遇到的case是：

- [0, 0, 1, 2, 0]

(在阐述想法，同时说出你考虑到了edge case, 加分！)

接下来就是最优的思路是了, 即：

When we multiply all values of arr before and after each index, we get our answer — the product of all the integers except `arr[i]`.


但是更容易解释的代码是，

![example](https://i.imgur.com/lRZ83qf.png)

``` python 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        if n == 0 or n == 1:
            return []
        
        left = [1] * n
        right = [1] * n 
        res = [None for _ in range(n)]
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        for k in range(n):
            res[k] = left[k] * right[k]
            
        return res 
```

这个基础上，再阐述：如果我想要优化空间，

> Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

这样，就可以更加简单说明最优解的做法。

