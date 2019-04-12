# Backtracking 

![Backtracking](https://i.imgur.com/2Y3D3fI.gif)

> **Backtracking** is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.[1][2]


## 基础知识

## 典型应用

- subset
- permutation 
- combination sum
- palindrome partitioning

## 最佳实践

### path: permutation(visited)
``` python
# remove `nums`, `res` if you write a nested function
def backtrack(path, nums, res):
	# base case 
	if len(path) == len(nums):
		res.append(path)
	# general case 
	for num in set(nums) - set(path):
		backtrack(path+[num], nums, res)
	return res 
```


### path: subset(order)

``` python 
# remove `nums`, `res` if you write a nested function
def backtrack(path, i, nums, res):
	# base case 
	res.append(path)
	# general case 
	for nxt in range(i, len(nums)):
		backtrack(path + [nums[nxt]], nxt+1, nums, res)
	return res 
```

### path: combination sum

``` python 
# with duplicate 
def backtrack(path, i, target, res, nums):
	# backtracking 
	if target < 0:
		return 
	# base case 
	if target == 0:
		res.append(path)
	# general case 
	for nxt in range(i, len(nums)):
		backtrack(path+[nums[nxt]], nxt, target-nums[nxt], res, nums)
	return res 
```

## 木桩训练

* [78. Subsets](https://leetcode.com/problems/subsets/): ？


## Explain


## Q&A

## Thanks