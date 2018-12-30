# Sorting 总结

|    排序算法    |思路 |  优缺点 | 应用场景| 典型题目 | 备注 | 
| ---------- | --- | ---------- | --- | --- | --- |
| quicksort | xx |runs 0(n**2) time in worst-case | 多数情况 | [sort color](https://leetcode.com/problems/sort-colors/description/) | xx |
| mergesort | xx | stable but not in-place | xx | xx | xx |
| heapsort | xx | in-place but not stable | nearly sorted | xx | xx |
| insertsort | xx | better for short arrays |  e.g. 10 or fewer elements | xx | xx |
| counting sort | xx | O(n)|  e.g. integers in the range [0..255] | xx | xx |

其他: merge/quick/heap/selection/insertion/bubble/counting/radix 

**备注**：

- An in-place sort is one which uses 0(1) space; 
- a **stable** sort is one where entries which are equal appear in their original order.


## 基础知识

1. A well-implemented **quicksort** is usually the best choice for sorting. 
2. Most sorting algorithms are not stable. **Merge sort**, carefully implemented, can be made stable.
3. Most sorting routines are based **on a compare function** that takes two items as input and returns -1 if the first item is smaller them the second item, 0 if they are equal and 1 otherwise. However, it is also possible to use **numerical attributes** directly, e.g., **in radix sort.**
4. **Heaps** can be helpful in sorting problems. Briefly, a max-heap (min-heap) stores keys drawn from an ordered set. It supports 0( log n) inserts and 0(1) time lookup for the maximum (minimum) element; the maximum (minimum) key can be deleted in 0( log n) time. 


![compare](https://i.imgur.com/ZyzWmIG.png)

**稳定性**：排序前后两个相等的数相对位置不变，则算法稳定。

**稳定性得好处**：从一个键上排序，然后再从另一个键上排序，第一个键排序的结果可以为第二个键排序所用。


* 1、堆排序、快速排序、希尔排序、直接选择排序**不是稳定**的排序算法；
* 2、基数排序、冒泡排序、直接插入排序、折半插入排序、归并排序是**稳定**的排序算法。

## 典型应用

Sorting problems come in two flavors: 
 
*  (1.) use sorting to **make subsequent steps in an algorithm simpler**, and 
*  (2.) design **a custom sorting routine.** 
  
 For the former, it's fine to use a library sort function, possibly with **a custom comparator**. For the latter, use a data structure like **a BST, heap, or array** indexed by values. [Problems 14.4 and 14.7]
 
The most natural reason to sort is if the inputs have **a natural ordering**, and sorting can be used as a preprocessing step to **speed up searching.** [14.5]

For **specialized input**, e.g., a very small range of values, or a small number of values, it's possible to sort in 0(n) time rather than 0(n log n) time. [Problems 6.1 and 14.7]

It's often the case that sorting can be implemented in **less space** than required by a brute-force approach. [Problem 14.2]


## 木桩训练

1. [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/): 引申：350(Fllow up)
2. [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) : 逆向思维，从右往左
3. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/):
4. Rend
5. [57. Insert Interval](https://leetcode.com/problems/insert-interval/description/)
6. [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/): sorting == a preprocessing step? Speed up searching!
7. partitioning and sorting an array with many repeated entries 
8. team photo day 1 
9. implement a fast sorting algorithm for lists
10. compute a salary threshold


