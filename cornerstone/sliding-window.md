# sliding window

![sliding window](https://i.imgur.com/pWFuBCj.png)

<center>在LinkedList中，就是<b>快慢指针</b>，在ArrayList中，就是<b>移动窗口</b>。</center>
	
<center>  在生活中，就是<b>骑驴找马</b>。 🦄  </center>
<center> <b> (maintain a job while looking for a better one)
  </b> </center>

## 1. 模版 
``` python 
def sliding_window(arr):

	longest = 0
	start = 0
	visited = {}
	# variable to count the condition 
	
	for i, num in enumerate(arr):
		# do sth. for num
	
		while not condition:
			# do sth. 
		  
		longest = max(longest, i - start + 1)
		
	return longest 
```

## 2. 典型题目

Check [76. Minimum Window Substring](https://willwang-x.github.io/2018/03/fast-and-slow)



## 3. 木桩训练

1. [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)	
1. [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/) : 快慢指针, 注意Dummy Node.
1. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
1. [159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)
1. [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)
2. [443. String Compression](https://leetcode.com/problems/string-compression/): write, ahchor and**** read  和26很像的题目
1. 438 Find All Anagrams in a String
1. [487. Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/description/)
1. [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)