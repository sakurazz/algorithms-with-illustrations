'''
# 6.4 Subset sums and knapsacks: adding a variable 

We’re seeing more and more that issues in scheduling provide a rich source of practically motivated algorithmic problems. So far we’ve considered problems in which requests are specified by a given interval of time on a resource, as well as problems in which requests have a duration and a deadline but do not mandate a particular interval during which they need to be done.

In this section, we consider a version of the second type of problem, with durations and deadlines, which is difficult to solve directly using the techniques we’ve seen so far. We will use dynamic programming to solve the problem, but with a twist: the “obvious” set of subproblems will turn out not to be enough, and so we end up creating a richer collection of subproblems. As we will see, this is done by adding a new variable to the recurrence underlying the dynamic program.


## 6.4.1 The problem:
n items {1,..., n}
wi 
Bound: W 

## 6.4.2 Solution 

W = 10
items = [2,3,6]

	(0,10)
1:2	(0,10) - (2,8)
2:3	(0,10), (3,7)  (2,8) (5,5)
3:6 (0,10),(6,4) (3,7) (9,1)  (2,8) (8,2)  (5,5) (5,5) 

 2^3 = 8


d(i, j)=max{ d(i-1, j), d(i-1,j-V[i-1]) + W[i-1]}

subsetSum(i) = max(subsetSum(i-1,W-items[i]), subsetSum(i-1, W))

i   W   V   0   1   2   3   4   5   6   7   8    9  10 
			0   0   0   0   0   0   0   0   0    0   0
a	2	2	0   0   2   2   2   2   2   2   2    2   2 
b	3	3	0   0   2   3   3   5   5   5   5    5   5   
c	6	6	0   0   2   3   3   5   6   6   8    8   8

dp[i][w] = max( dp[i-1][w], dp[i-1][w-items[]]   )

'''



class Solution(object):

	def __init__(self):
		pass

	def knapsacks(self, items, W):
		dp = [[0 for _ in range(W+1)] for _ in range(len(items)+1)]
		for i in range(1, len(items)+1):
			for w in range(1, W+1):
				print("items:",i,", weight:",w,", value:",items[i-1])
				if w - items[i-1] >= 0:
					dp[i][w] = max(dp[i-1][w-items[i-1]] + items[i-1], dp[i-1][w])
				else:
					dp[i][w] = dp[i-1][w]
				for d in dp:
					print(d)
				print()
		return dp[len(items)][W]




items = [2,3,6]
W = 10
print(Solution().knapsacks(items, W))

