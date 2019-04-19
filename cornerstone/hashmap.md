# Hashmap 

<img src="https://i.imgur.com/l1598o9.gif" alt="hash" width="500"/> <br> 

by [Inside python dict](https://just-taking-a-ride.com/inside_python_dict/chapter2.html)

## 基础知识

- deal with exception
- collision 
- hash function
- open hashing or closed hashing
- loading factor

## 典型应用

* cache: [523](https://leetcode.com/problems/continuous-subarray-sum/description/)

## 最佳实践

- prefix sum
- lowercase hashmap
- design a hashmap

### prefix sum

``` python 
def max_subarray_len(nums: List[int], k: int) -> int:
    prefix_sum = {0: -1} # sum_ : index
    sum_ ,size = 0, 0
    for i, num in enumerate(nums):
        sum_ += num
        if sum_ - k in prefix_sum:
            size = max(size, i - prefix_sum[sum_ - k])
        if sum_ not in prefix_sum:
            prefix_sum[sum_] = i 
    return size
```

### lowercase hashmap

``` python 
def group_anagrams(self, strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())
```

## 木桩训练

- 1 Two Sum
- 18 4Sum 
- 36 Valid Sudoku
- 49 Group Anagrams 
- 136 Single Number
- 138 Copy List with Random Pointer 
- 149 Max Points on a Line 
- 166 Fraction to Recurring Decimal 
- 170 Two Sum III - Data structure design 
- 204 Count Primes 
- 217 Contains Duplicate 
- 325 Maximum Size Subarray Sum Equals k (类型)
- 350 Intersection of Two Arrays II 
- 454 4Sum II 
- 535 Encode and Decode TinyURL

## More

- [instant-runoff voting](https://repl.it/@WillWang42/instant-runoff-voting): the hashtable is a good way to speed up calculation