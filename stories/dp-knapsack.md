# DP knapsack series 


>  Given a set of items, each with a **weight** and a **value**, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total **value** is **as large as possible**. 
> 
> -- *[Knapsack problem](https://www.wikiwand.com/en/Knapsack_problem)*


## 1. 0/1 Knapsack  

> Given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items such that sum of the weights of those items of given subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it **(0-1 property)**.

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

``` python 

# https://repl.it/@WillWang42/dp-knapsack-01
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapsack(W, weight, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 

    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weight[i-1] <= w: 
                # pick it or not 
                K[i][w] = max(val[i-1] + K[i-1][w-weight[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W] 

val = [6, 10, 12] 
weight = [1, 2, 3] 
W = 5
n = len(val) 
print(knapsack(W, weight, val, n)) 

```

## 2. knapsack with infinite items   
```python 
```


## 3. knapsack with repetitions 
```python
```

## 木桩训练

* [322. Coin Change](https://leetcode.com/problems/coin-change/description/)
* [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)
* [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/description/)
* [494. Target Sum](https://leetcode.com/problems/target-sum/description/)
* [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/description/)

## Thanks

* [0-1 Knapsack Problem | DP-10](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
* [背包问题九讲](https://www.kancloud.cn/kancloud/pack/70125)
* [Coursera: Knapsack with Repetitions](https://www.coursera.org/lecture/algorithmic-toolbox/knapsack-with-repetitions-uYVzW)