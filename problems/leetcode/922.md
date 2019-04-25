# 922 Sort Array By Parity II

## 问题

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

```
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

## 思路


**启发：**

- 用指针去指向位置，而不用开辟新空间
- 对于二元问题，只用排好一个位置，那么另一个位置，就自动排好了！
- 对于二元问题，**何时交换？** 找到两个都不对的位置，交换即可。

``` python 
class Solution1(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = [None for _ in range(len(A))]
        odd = 1
        even = 0 
        for num in A:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2
        return ans 
```
### 交换的时刻？

``` python 
class Solution2(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
```

## Interview moment for 922

**The brute force solution is** just to read all the even integers and put them into places ans[0], ans[2], ans[4], and so on. 

Then, read all the odd integers and put them into places ans[1], ans[3], ans[5], etc.
 
How can we improve our solution? We may want to pursue a solution where we modify the original array A **in place**.

First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too. So **let's only focus on** A[0], A[2], A[4], ...

**Ideally**, we would like to have some **partition** where everything to the left is already correct, and everything to the right is undecided.

**Indeed**, **this idea works** if we separate it into two **slices** even = A[0], A[2], A[4], ... and odd = A[1], A[3], A[5], .... Our **invariant** will be that everything less than `i` in the even slice is correct, and everything less than `j` in the odd slice is correct.


For each even `i`, let's make `A[i]` even. To do it, we will iterate the even slice until we find an odd element. Then we **pass** `j` through the odd slice until we find an even element, then **swap**. Our **invariant** is maintained, so the algorithm is correct.
