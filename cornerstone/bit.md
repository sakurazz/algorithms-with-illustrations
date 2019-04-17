# Bit 

<img src="https://i.imgur.com/S6s8tb6.png" alt="bit" width="200"/>

## 基础知识

Questions involving binary representations and bitwise operations are asked sometimes and you must be absolutely familiar with how to convert a number **from decimal form into binary form (and vice versa)** in your chosen programming language.

## 典型应用

- XOR

## 最佳实践

Some helpful utility snippets:

- Test k<sup>th</sup> bit is set: `num & (1 << k) != 0`.
- Set k<sup>th</sup> bit: `num |= (1 << k)`.
- Turn off k<sup>th</sup> bit: `num &= ~(1 << k)`.
- Toggle the k<sup>th</sup> bit: `num ^= (1 << k)`.
- To check if a number is a power of 2, `num & num - 1 == 0`.

``` python
# binary/hexadecimal to decimal 
int('11', 2) # 3
int('F', 16) # 15 

# decimal to binary
bin(10)[2:] # '1010'
```

### corner cases

* Check for overflow/underflow.
* Negative numbers.

## 木桩训练

- [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
- [268. Missing Number](https://leetcode.com/problems/missing-number/)
- [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [411. Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/)
- [1017. Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)

## Explain

- [268. Missing Number](https://leetcode.com/problems/missing-number/)
	- We can **harness the fact that XOR** is its own inverse to find the missing element in linear time.
	- Because we know that `nums` contains n numbers and that it is missing exactly one number on the range [0..n−1], we know that *n* definitely replaces the missing number in `nums`. Therefore, if we initialize an integer to n and XOR it with every index and value, we will be left with the missing number. 




## Q&A

## Thanks 

- [handbooks](https://github.com/yangshun/tech-interview-handbook/tree/master/algorithms)