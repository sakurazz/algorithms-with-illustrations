# String 

<img src="https://i.imgur.com/1MzpsFt.png" alt="string" width="200"/> 


## 基础知识

Similar to arrays, string problems often have simple brute-force solutions that use O(n) space solution, but subtler solutions that use the string itself to **reduce space** **complexity**.

Understand the implications of a string type which is **immutable**, e.g., the need to allocate a new string when concatenating immutable strings. Know alternatives to immutable strings, e.g., an array of characters or a `StringBuilder` in Java.

Updating a mutable string from the front is slow, so see if it's possible to **write values from the back**.

## 典型应用

1. **anagram**: sort, hashmap or counter 
2. **palindrome**: a == a[::-1] 
3. **substring**: counter, sliding window
4. **match**: 
	- KMP? 
	- Rabin Karp? 
	- wildcards, [10](https://leetcode.com/problems/regular-expression-matching/)
5. **search**: trie, [212](https://leetcode.com/problems/word-search-ii/)

## 最佳实践

- counter 
- trie 
- suffix tree
- Rabin Karp
- [KMP](http://whocouldthat.be/visualizing-string-matching/)

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
or simpler 

``` python
_trie = lambda : collections.defaultdict(_trie)
```

``` python
def words_trie(words):
	trie = _trie()
	for _, word in enumerate(words):
		functools.reduce(dict.__getitem__, word, trie)["#"] = None 
```

### KMP(dive deep)

``` python
def kmp_matcher(pattern, text):
    pi = compute_prefix_function(pattern)
    matched = 0
    for i in range(len(text)):
        while matched > 0 and pattern[matched] != text[i]:
            matched = pi[matched - 1]
        if pattern[matched] == text[i]:
            matched += 1
        if matched == len(pattern):
            return i + 1 - len(pattern)
    return -1

def compute_prefix_function(pattern):
    pi = [0] * len(pattern)
    matched = 0
    for i in range(1, len(pattern)):
        while matched > 0 and pattern[i] != pattern[matched]:
            matched = pi[matched - 1]
        if pattern[i] == pattern[matched]:
            matched += 1
        pi[i] = matched
    return pi
```

## 木桩训练

- [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
- [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- [67. Add Binary](https://leetcode.com/problems/add-binary/)