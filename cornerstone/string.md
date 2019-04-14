# String 



## 基础知识

Similar to arrays, string problems often have simple brute-force solutions that use 0(n) space solution, but subtler solutions that use the string itself to **reduce space** **complexity** to [Problems 7.6 and 7.4]

Understand the **implications** of a string type which is **immutable**, e.g., the need to allocate a new string when concatenating immutable strings. Know alternatives to immutable strings, e.g., an array of characters or a StringBuilder in Java. [Problem 7.6]

Updating a mutable string from the front is slow, so see if it's possible to **write values from the back**. [Problem 7.4]

## 典型应用

- anagram: 
	- sort, hashmap or counter 
- palindrome
 	- a == a[::-1] ? 
- match: KMP
- substring 

## 最佳实践

- counter 
- trie 
- prefix trie?
- Rabin Karp
- KMP 

### counter

``` python
# counter instead of hashmap for `a-z`
counter = [0 for _ in range(26)]
for c in letters:
	counter[ord(c)-ord('a')] += 1

# Space complexity is O(1) instead O(n). 
# Cause there  the upper bound is the range of characters, 
# which is usually a fixed constant of 26. 
```
### trie 

``` python
# simple trie used for preprocess
trie = {}
words= ['apple', 'banana', 'cherry']

cur = trie
for word in words:
	for c in word:
		if c not in cur: cur[c] = {}
		cur = cur[c]
```

## 木桩训练

- [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
- [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- [67. Add Binary](https://leetcode.com/problems/add-binary/)