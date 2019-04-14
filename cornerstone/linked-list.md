
# Linked list 


![linked list](https://i.imgur.com/xwQ842u.png)

> A linked list is a linear data structure, the elements are not stored **at contiguous memory locations**. The elements in a linked list are linked using **pointers**.

## 基础知识

List problems often have a simple brute-force solution that uses 0(n) space, but a subtler solution that uses **the existing list nodes** to reduce space complexity to 0(1). 

Very often, a problem on lists is conceptually simple, and is more about **cleanly coding what's specified**, rather than designing an algorithm.

Consider using **a dummy head** (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely. 

It's easy to forget **to update next** (and previous for double linked list) for the head and tail.

Algorithms operating on singly linked lists often benefit from using **two iterators**, one ahead of the other, or **one advancing quicker than the other**. 
 
## 典型应用

- deletion O(1): moditfy the value or pointer 
- dummy node: [2](https://leetcode.com/problems/add-two-numbers/description/)
- reverse: [25](https://leetcode.com/problems/reverse-nodes-in-k-group/description/), [92](https://leetcode.com/problems/reverse-linked-list-ii/description/), [206](https://leetcode.com/problems/reverse-linked-list/description/)
- partition: merge two lists
- linked list ~= array 
- two pointer (fast/slow pointers)
	- get the kth from last node 
	- detect cycle 
	- getting the middle node 

## 最佳实践

- [create](https://repl.it/@WillWang42/linked-list)
- insert (front, given node, end)
- deletiton: modify(values, LC450) or change(pointers)
- sort([LC147](https://leetcode.com/problems/insertion-sort-list/description/)) 
- adding a dummy node ([LC117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/), LC146)
- recursively (reverse linked-list)
- count, **reverse**, find the middle, merge

### corner cases

- `None`
- Single node 
- Two nodes
- Linked list has cycle. Clarify with the interviewer whether there can be a cycle in the list. Usually the answer is no.

## 木桩训练

* [ ] 将《element》中的习题整理出来。


## Explain

## Q&A

## Thanks 

