# DP knapsack series 


>  Given a set of items, each with a **weight** and a **value**, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total **value** is **as large as possible**. 
> 
> -- *[Knapsack problem](https://www.wikiwand.com/en/Knapsack_problem)*


## 1. 0/1 Knapsack  

![example](https://i.imgur.com/Z4qcav2.jpg)

> Given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items such that sum of the weights of those items of given subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it **(0-1 property)**.

**f[i][c] = max( f[i-1][c], f[i-1][c-wlist[i]] + vlist[i] )** 

`f[i][v]` 为有`i`个物品，背包容量为`c`(capacity)时获得的最好价值。
 
*  情况一: 第i件不放进去，这时所得价值为:  `f[i-1][c]`
*  情况二: 第i件放进去后，这时所得价值为:  `f[i-1][c-wlist[i]] + vlist[i]`


``` python 

# https://repl.it/@WillWang42/dp-knapsack
# Returns the maximum value that can be put in a knapsack of capacity `c`
def knapsack_01(capacity, wlist, vlist): 
    n = len(wlist)
    K = [[0] * (capacity+1) for _ in range(n+1)] 

    # Build table K[][] in bottom up manner 
    for i in range(1, n+1): 
        for c in range(1, capacity+1): 
            which = i - 1 # cause vlist starts from 0 
            if wlist[which] <= c: 
                # pick it or not 
                K[i][c] = max(vlist[which] + K[i-1][c-wlist[which]],  K[i-1][c]) 
            else: 
                K[i][c] = K[i-1][c]  

    return K[n][capacity] 

vlist = [4, 5, 6] 
wlist = [3, 4, 5] 
capacity = 10
print(knapsack_01(capacity, wlist, vlist))  # 11

```

### Follow up 1: 如果我们只用一维DP, 如何做呢？

核心问题：我们在不能覆盖之后会使用的新数据。所以，我们倒序更新DP数组，从背包容量`n到1`更新，如果反之，我已经得到对于第i件物品：

> i == 2, K = [0, 0, 0, 4, 5, 5, 5, 9, 9, 9, 9]

当物品 `i = 3` 时，如果我们**正序**更新，那么

> K[5] = max(K[5 - wlist[3]] + vlist[3], K[5])

这时已经改变了K[5]的值，但是如果后面，比如，K[10] 要用到K[5]时，这是K[5]已经是 `i == 3`的值，而不是 `i == 2` 的值了， 但是我们想要是 `i == 2` 时 K[5]的值。

而**倒序**更新则不会影响，因为K[5]永远不会是用到K[10]的值。

``` python 
def knapsack_01_1d(capacity, wlist, vlist): 
    n = len(wlist)
    K = [0] * (capacity+1) 

    for i in range(n): 
        for c in range(capacity, 0, -1): 
            if wlist[i] <= c: 
                # pick it or not 
                K[c] = max(vlist[i] + K[c-wlist[i]],  K[c]) 

    return K[-1] # 11
```

### Follow up 2: 如果使用recursive的方法做呢？

即自上往下做，如下图所示：

```
In the following recursion tree, K() refers to knapSack().  The two 
parameters indicated in the following recursion tree are n and W.  
The recursion tree is for following sample inputs.
wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}

                       K(3, 2)         ---------> K(n, W)
                   /            \ 
                 /                \               
            K(2,2)                  K(2,1)
          /       \                  /    \ 
        /           \              /        \
       K(1,2)      K(1,1)        K(1,1)     K(1,0)
       /  \         /   \          /   \
     /      \     /       \      /       \
K(0,2)  K(0,1)  K(0,1)  K(0,0)  K(0,1)   K(0,0)
Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.
```

```python
# Time: O(2^n) where n = len(wlist)
# Space: O(n)

def helper(n, c, wlist, vlist, selected):
    if n == 0 or c == 0:
      return 0
    for i in range(n-1, -1, -1):
      if wlist[i] > c:
        return helper(n-1, c, wlist, vlist, selected)
      else:
        p_yeah = vlist[i] + helper(n-1, c-wlist[i], wlist, vlist, selected)
        p_nope = helper(n-1, c, wlist, vlist, selected)
        if p_yeah > p_nope:
          selected[i] = 1
          return p_yeah
        else:
          return p_nope

def knapsack_01_recursive(capacity, wlist, vlist):
    n = len(wlist)
    selected = [0] * n
    return helper(n, capacity, wlist, vlist, selected)
```

### 实战1.1: LC416. Partition Equal Subset Sum

This problem is essentially let us to find whether there are several numbers in a set which are able to sum to a specific value (in this problem, the value is sum/2).

> For each number, we can **pick it or not.** 

Let us assume dp[i][j] means whether the specific sum `j` can be gotten from the first `i` numbers. 

If we can pick such a series of numbers from 0-i whose sum is `j`, `dp[i][j]` is true, otherwise it is false.

**Base case**: `dp[0][0]` is true; (zero number consists of sum 0 is true)

**Transition function**: For each number, 

- If we pick nums[i]. `dp[i][j] = dp[i-1][j-nums[i]]`, which represents that j is composed of the current value nums[i] and other previous numbers. 
- if we don't pick it, `dp[i][j] = dp[i-1][j]`, which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]). 

Thus, the transition function is `dp[i][j] =  dp[i-1][j-nums[i]] | dp[i-1][j]`. 

If we use 1-D solution, the transition function would be

`dp[j] = dp[j-nums[i]] | dp[j]` 

``` python 
# Time: O(n * half) where n = len(nums), half = sum(nums) / 2
# Space: O(half)
# 416. Partition Equal Subset Sum

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        quotient, remainder =  divmod(sum(nums), 2)
        if remainder == 1: return False 
        
        dp = [True] + [False for _ in range(quotient)]
        
        for i in range(len(nums)):
            for j in range(quotient, nums[i]-1, -1):
                dp[j] = dp[j-nums[i]] | dp[j]
        return dp[-1]
```



## 2. knapsack with infinite items   

> *完全背包: 有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。*


**f[c] = max(f[c], f[c-wlist[i]] + vlist[i])**, where  0 <= i < len(wlist)

`f[n]` 为背包容量为`c`(capacity)时的获得最好的价值
 
 不同于01背包，在背包容量为c时，所有物品都可以选择, 所以如果知道f[1] ... f[c-1]的值，那么求f[c]，即把所有放入背包试一下，取最大值即可。

```python
def knapsack_infinite(capacity, wlist, vlist):
    n = len(wlist)
    K = [0] * (capacity+1)

    for c in range(1, capacity+1):
      for i in range(n):
            if wlist[i] <= c: 
                # pick it or not 
                K[c] = max(vlist[i] + K[c-wlist[i]],  K[c]) 
    print(K)
    return K[-1]

vlist = [4, 5, 6] 
wlist = [3, 4, 5] 
capacity2 = 21

print(knapsack_infinite(capacity2, wlist, vlist))  # 28
# [0, 0, 0, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28]
# 4/3 has the best value for its weight, thus (21/3) * 4 = 28 
```
### 实战2.1：LC322

类似的题目，有**LC322. Coin Change**, 区别在于求“最少”, 但本质的思路还是一样： 

> pick it or not 

``` python 
# Time: O( amount * len(coins) ) 
# Space: O(amount)
# 322. Coin Change

'''
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Amount:  0 1 2 3 4 5 6 7 8 9 10 11
         0 x x x x x x x x x x  x
           1 1 2 2 1 2 2 3 3 2  3        

dp[3] = min(dp[3], dp[3-1] + 1) = 2
dp[3] = min(dp[3], dp[3-2] + 1) = 2
   
Which is better? use it or not.
'''

def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # if amount == 0: return 0 
    if not coins:   return -1
    
    dp = [0] + [float("inf") for _ in range(amount + 1)]
    
    for v in range(1, amount + 1):
        for c in coins:
            if c <= v:
                dp[v] = min(dp[v], dp[v-c]+1) 
       
    return dp[amount] if dp[amount] != float("inf") else -1

```
### 实战2.2: LC518

还有 **LC518. coin change 2**, 其思路还是一样：

> 使用新的硬币，能够产生新的combinations的有什么。

```python 
# Time: O(n * v) where n = len(coins) and v = amount
# Space: O(amount)

def change2(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    record = [1] + [0]*amount
    for coin in coins:
        for v in range(coin, amount+1):
            record[v] += record[v-coin] # use the coin 
    return record[amount]
```

## 3. knapsack with repetitions 
> 多重背包: 有N种物品和一个容量为V的背包。第i种物品最多有n[i]件可用，每件费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。 

简单的做法，是把多重背包变成01背包去做。

``` python 
# Time:  O( sum(nlist[i]) * c )
# space: O(c)

def knapsack_bounded(capacity, wlist, vlist, nlist):
    n = len(wlist)
    K = [0] * (capacity+1) 

    for i in range(n): 
      for _ in range(nlist[i]): # unfold it to 01 knapsack problem 
        for c in range(capacity, 0, -1): 
            if wlist[i] <= c: 
                # pick it or not 
                K[c] = max(vlist[i] + K[c-wlist[i]],  K[c]) 

    print(K)   
    return K[-1]   
```


## 木桩训练

* [322. Coin Change](https://leetcode.com/problems/coin-change/description/)
* [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)
* [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/description/)
* [494. Target Sum](https://leetcode.com/problems/target-sum/description/)
* [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/description/)

## Thanks

* [JavaScript 背包问题详解](http://web.jobbole.com/93722/): 详细的背包解法
* [0-1 Knapsack Problem | DP-10](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
* [Book: knapsack problems](http://www.or.deis.unibo.it/knapsack.html): 一本讲个背包问题各种情况的书
* [背包问题九讲](https://www.kancloud.cn/kancloud/pack/70125)： 觉得写的并不好，价值在于总结了各种背包问题
* [Coursera: Knapsack with Repetitions](https://www.coursera.org/lecture/algorithmic-toolbox/knapsack-with-repetitions-uYVzW)
* [背包之01背包、完全背包、多重背包详解 — TankyWoo](http://www.wutianqi.com/?p=539)
* [Knapsack problem](https://rosettacode.org/wiki/Knapsack_problem): 各种语言写的solutions
* [淺談多重背包問題 (Multiple Knapsack Problem) 優化那些事](http://morris821028.github.io/2016/12/18/jg-20008/): 内容比较深，有空看看
* [多重背包 O(VN) 做法 | 单调队列](https://www.zybuluo.com/RabbitHu/note/857837): 单调队列的解法需要再看一下
* [多重背包O(N*V)算法详解（使用单调队列）](http://www.cppblog.com/flyinghearts/archive/2010/09/01/125555.html)