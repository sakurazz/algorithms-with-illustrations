# Trie 总结

[](http://www.allisons.org/ll/AlgDS/Tree/PICS/trie.gif)


## 基础知识

Tries is a tree that stores strings. Maximum number of children of a node is equal to size of alphabet. Trie supports search, insert and delete operations in O(L) time where L is length of key.

### Why Trie? :-

1. With Trie, we can insert and find strings in O(L) time where L represent the length of a single word. This is obviously faster that BST. This is also faster than Hashing because of the ways it is implemented. We do not need to compute any hash function. No collision handling is required (like we do in open addressing and separate chaining)
2. Another advantage of Trie is, we can easily print all words in alphabetical order which is not easily possible with hashing.
3. We can efficiently do prefix search (or auto-complete) with Trie.

### Issues with Trie :-
The main disadvantage of tries is that they need lot of memory for storing the strings. For each node we have too many node pointers(equal to number of characters of the alphabet), If space is concern, then Ternary Search Tree can be preferred for dictionary implementations. In Ternary Search Tree, time complexity of search operation is O(h) where h is height of the tree. Ternary Search Trees also supports other operations supported by Trie like prefix search, alphabetical order printing and nearest neighbor search.

The final conclusion is regarding tries data structure is **that they are faster but require huge memory for storing the strings.**

## Reference

[Geeks Trie ](https://www.geeksforgeeks.org/advantages-trie-data-structure/)

## 木桩训练

- [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)
- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
- [642. Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/description/)
- [211. Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/description/)