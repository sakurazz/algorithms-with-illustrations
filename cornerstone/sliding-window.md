# sliding window

![sliding window](https://i.imgur.com/pWFuBCj.png)

## 基础知识

在LinkedList中，就是<b>快慢指针</b>，

在ArrayList中，就是<b>移动窗口</b>。

在生活中，就是<b>骑驴找马</b>。 🦄  

## 典型应用

- 快慢指针
- string

## 最佳实践

### longest 

``` python 
def sliding_window(arr):

	longest = 0
	head = 0
	visited = {}
	# variable to count the condition 
	
	for tail, num in enumerate(arr):
		# do sth. for num
	
		while not condition:
			# do sth. 
		  
		longest = max(longest, tail - head + 1)
		
	return longest 
```

### shortest 

``` python 
def sliding_window(arr):

	shortest = 0
	head = 0
	seats = {}
	count = 0 
	# variable to count the condition 
	
	for tail, num in enumerate(arr):
		# do sth. for num
	
		while condition:
			shortest = min(shortest, tail - head + 1)
			# do sth.
			
	return shortest 
```

## 木桩训练

1. [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)	
1. [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/) : 快慢指针, 注意Dummy Node.
1. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
1. [159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)
1. [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)
2. [443. String Compression](https://leetcode.com/problems/string-compression/): write, ahchor and**** read  和26很像的题目
1. 438 Find All Anagrams in a String
1. [487. Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/description/)
1. [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)
2. LC76

## Explain 

- [LC76. Minimum Window Substring](https://www.pramp.com/challenge/wqNo9joKG6IJm67B6z34)
	- We scan the input string `str` from left to right while maintaining two indices - `headIndex` and `tailIndex`.
	- At each iteration, we **examine** a temporary substring `[str.charAt(headIndex),..., str.charAt(tailIndex)]` and **keep a copy of the shortest** valid substring we’ve seen so far. **Said differently**, we keep incrementing `tailIndex` until the above substring contains every unique character in `arr`.
	- If the size of **the resulting substring** equals to `arr.length` then we return it since **by definition** there can’t be a shorter valid substring (otherwise, it’ll be missing 1 or more unique characters from arr).
	- **Once we found a valid substring, we increment `headIndex` as long the substring remains valid.** At every increment we also **check if the current valid substring** is shorter than the previously kept one. If it is, we **update result to be the current substring**.
	- We keep repeating the above steps in a loop until we either reach the end of the input string `str` or return the shortest valid substring, **whichever comes first.**
	- To examine the **validity** of `str` substrings we use 2 **counters**:
		- `uniqueCounter` (Integer) - the number of unique characters of `arr` that our current substring contains.
		- `countMap` (Map/Hash Table) - the number of occurrences of each character of `arr` in our current substring.
	- source: pramp
 

## Q&A

## Thanks