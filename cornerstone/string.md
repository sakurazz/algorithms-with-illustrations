# String 



## 基础知识

Similar to arrays, string problems often have simple brute-force solutions that use 0(n) space solution, but subtler solutions that use the string itself to **reduce space** **complexity** to [Problems 7.6 and 7.4]

Understand the **implications** of a string type which is **immutable**, e.g., the need to allocate a new string when concatenating immutable strings. Know alternatives to immutable strings, e.g., an array of characters or a StringBuilder in Java. [Problem 7.6]

Updating a mutable string from the front is slow, so see if it's possible to **write values from the back**. [Problem 7.4]

## 典型应用

- anagram
- palindrome
- match: KMP 

## 最佳实践

## 木桩训练